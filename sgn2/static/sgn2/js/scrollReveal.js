document.addEventListener("DOMContentLoaded", function ()  {
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: [0.1, 1.0]
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                entry.classList.remove('hidden');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.element').forEach(element => {
        observer.observe(element);
    });
});