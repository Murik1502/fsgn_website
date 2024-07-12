function isElementInViewport(el, percentVisible) {
    const rect = el.getBoundingClientRect();
    const windowHeight = window.innerHeight || document.documentElement.clientHeight;
    const elementHeight = el.offsetHeight;
    const visibleHeight = (elementHeight * percentVisible) / 100;

    return (rect.top + visibleHeight >= 0 && rect.left >= 0 && rect.bottom - visibleHeight <= windowHeight &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

function checkVisibility() {
    const container = document.querySelector('.company_carousel_wrap');
    const elements = document.querySelectorAll('.company_layouts');

    if (isElementInViewport(container, 15)) {
        elements.forEach(element => {
            element.classList.add('visible');
        });
        document.querySelector('.company_carousel').classList.add('animate');
        window.removeEventListener('scroll', checkVisibility);
        window.removeEventListener('load', checkVisibility);
    }
}

window.addEventListener('scroll', checkVisibility);
window.addEventListener('load', checkVisibility);
