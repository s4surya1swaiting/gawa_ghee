const { test, expect } = require('@playwright/test');

test.describe('Gawa Ghee B2B Website E2E Tests', () => {

    test('Homepage loads correctly and has required elements', async ({ page }) => {
        await page.goto('http://localhost:8000/index.html');
        await expect(page).toHaveTitle(/Gawa Ghee | Pure Ghee Manufacturer/);
        
        // Verify branding header exists
        const logo = page.locator('.logo h2');
        await expect(logo).toContainText('GAWA GHEE');
        
        // Verify key sections are present
        await expect(page.locator('text=Why Institutions Choose Us')).toBeVisible();
        await expect(page.locator('text=Built for Scale & Compliance')).toBeVisible();
        
        // Verify newly added sections are present
        await expect(page.locator('text=Curated Commercial Preview')).toBeVisible();
        await expect(page.locator('text=Trusted Quality, Proven at Scale')).toBeVisible();
        await expect(page.locator('text=Verified Business Validation')).toBeVisible();

        // Verify tracking tags and schema exist in Head
        const schemaScript = page.locator('script[type="application/ld+json"]');
        await expect(schemaScript).toHaveCount(1);
        
        // Verify floating WhatsApp button is visible
        const whatsappBtn = page.locator('.floating-wa');
        await expect(whatsappBtn).toBeVisible();
    });

    test('Desktop Navigation Links work correctly', async ({ page }) => {
        await page.goto('http://localhost:8000/index.html');
        
        // Click on Products
        await page.click('nav.main-nav >> text=Products');
        await expect(page).toHaveURL(/products.html/);
        
        // Click on Our Story
        await page.click('nav.main-nav >> text=Our Story');
        await expect(page).toHaveURL(/our-story.html/);
        
        // Click on Contact Us
        await page.click('nav.main-nav >> text=Contact Us');
        await expect(page).toHaveURL(/contact.html/);
    });

    test('Mobile viewport layout collapses and hamburger menu toggles navigation', async ({ page }) => {
        await page.setViewportSize({ width: 375, height: 667 });
        await page.goto('http://localhost:8000/index.html');
        
        const navToggle = page.locator('.mobile-nav-toggle');
        await expect(navToggle).toBeVisible();
        
        const navMenu = page.locator('.main-nav');
        await expect(navMenu).not.toHaveClass(/is-open/);
        
        // Toggle open
        await navToggle.click();
        await expect(navMenu).toHaveClass(/is-open/);
        
        // Toggle close
        await navToggle.click();
        await expect(navMenu).not.toHaveClass(/is-open/);
    });

    test('B2B contact form inputs validation and alert on submit', async ({ page }) => {
        await page.goto('http://localhost:8000/contact.html');
        
        const form = page.locator('#b2b-contact-form');
        await expect(form).toBeVisible();
        
        // Form submission triggers an alert
        page.on('dialog', async dialog => {
            expect(dialog.message()).toContain('Form successfully submitted!');
            await dialog.accept();
        });
        
        // Fill form fields
        await page.fill('#fullName', 'Jane Supplier');
        await page.fill('#companyName', 'HoReCa Wholesale Ltd');
        await page.fill('#phone', '9876543210');
        await page.fill('#email', 'procurement@horecawholesale.com');
        await page.selectOption('#operationType', 'horeca');
        await page.fill('#requirement-context', 'Looking for 500kg per month bulk packing.');
        
        // Submit
        await page.click('button[type="submit"]');
    });

    test('Dynamic SKU parameter routing pre-fills the enquiry context', async ({ page }) => {
        // Navigate to contact page with sku parameter
        await page.goto('http://localhost:8000/contact.html?sku=Classic-1L-Tin');
        
        const contextTextarea = page.locator('#requirement-context');
        await expect(contextTextarea).toHaveValue(/I am interested in bulk purchasing for SKU: Classic-1L-Tin/);
        
        // Verify from Products page navigation
        await page.goto('http://localhost:8000/products.html');
        
        // Click enquire now on the 1L Tin product card
        const card = page.locator('.product-card:has-text("Classic Pure Cow Ghee")');
        const enquireBtn = card.locator('text=Enquire Now');
        
        await enquireBtn.click();
        
        // Verify routing and automatic parameter fill
        await expect(page).toHaveURL(/contact.html\?sku=Classic-1L-Tin/);
        await expect(contextTextarea).toHaveValue(/I am interested in bulk purchasing for SKU: Classic-1L-Tin/);
    });

    test('Pricing Control (MRP) displays transparently on homepage and products grid', async ({ page }) => {
        // Check homepage previews
        await page.goto('http://localhost:8000/index.html');
        const previewCard = page.locator('.product-card:has-text("Commercial Kitchen Supply")');
        await expect(previewCard.locator('.product-price')).toContainText('MRP: ₹9,499');

        // Check products grid
        await page.goto('http://localhost:8000/products.html');
        const gridCard = page.locator('.product-card:has-text("Premium Danadar Gawa Ghee")');
        await expect(gridCard.locator('.product-price')).toContainText('MRP: ₹349');
    });
});
