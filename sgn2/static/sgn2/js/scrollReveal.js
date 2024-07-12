function isElementInViewport(el, percentVisible) {
    const rect = el.getBoundingClientRect();
    const windowHeight = window.innerHeight || document.documentElement.clientHeight;
    const elementHeight = el.offsetHeight;
    const visibleHeight = (elementHeight * percentVisible) / 100;

    return (
        rect.top + visibleHeight >= 0 &&
        rect.left >= 0 &&
        rect.bottom - visibleHeight <= windowHeight &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

function resetAnimation(elements, carousel) {
    elements.forEach(element => {
        element.classList.remove('visible');
        void element.offsetWidth;
    });
    carousel.classList.remove('animate');
    void carousel.offsetWidth;
}

function checkVisibility(containerSelector, elementsSelector, carouselSelector, percentVisible) {
    const container = document.querySelector(containerSelector);
    const elements = document.querySelectorAll(elementsSelector);
    const carousel = document.querySelector(carouselSelector);

    if (isElementInViewport(container, percentVisible)) {
        elements.forEach(element => {
            element.classList.add('visible');
        });
        carousel.classList.add('animate');
    } else {
        resetAnimation(elements, carousel);
    }
}

function checkVisibilityHandler() {
    checkVisibility('#container1 .company_carousel_wrap', '#container1 .company_layouts', '#container1 .company_carousel', 15);
    checkVisibility('#container2 .company_carousel_wrap', '#container2 .company_layouts', '#container2 .company_carousel', 15);
}

window.addEventListener('scroll', checkVisibilityHandler);
window.addEventListener('load', checkVisibilityHandler);
