document.addEventListener('DOMContentLoaded', () => {
    // Mobile Navigation Toggle
    const navToggle = document.querySelector('.mobile-nav-toggle');
    const mainNav = document.querySelector('.main-nav');
    
    if(navToggle && mainNav) {
        navToggle.addEventListener('click', () => {
            mainNav.classList.toggle('is-open');
        });
    }

    // Scroll Animations (Intersection Observer)
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target); // Only animate once
            }
        });
    }, observerOptions);

    const animatedElements = document.querySelectorAll('.animate-on-scroll');
    animatedElements.forEach(el => observer.observe(el));

    // Dynamic Header Background on Scroll
    const header = document.querySelector('.global-header');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('is-scrolled');
        } else {
            header.classList.remove('is-scrolled');
        }
    });

    // Populate SKU in Contact Form if redirected from Product Page
    const contactForm = document.getElementById('b2b-contact-form');
    if (contactForm) {
        const urlParams = new URLSearchParams(window.location.search);
        const skuParam = urlParams.get('sku');
        if (skuParam) {
            // Select matching product option
            const productField = document.getElementById('productSelect');
            if (productField) {
                const matchedOption = Array.from(productField.options).find(opt => opt.value === skuParam);
                if (matchedOption) {
                    productField.value = skuParam;
                }
            }
            // Populate additional details
            const contextField = document.getElementById('additionalDetails');
            if (contextField) {
                contextField.value = `I am interested in bulk purchasing for SKU: ${skuParam}. Please provide pricing details.`;
            }
        }
    }
});
