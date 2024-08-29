document.addEventListener('DOMContentLoaded', function() {
    const heroes = document.querySelectorAll('.hero-section');

    function updateBackgroundImages() {
        const screenWidth = window.innerWidth;
        heroes.forEach(hero => {
            const desktopImg = hero.getAttribute('data-desktop-img');
            const mobileImg = hero.getAttribute('data-mobile-img');
            hero.style.backgroundImage = screenWidth <= 768 ? `url('${mobileImg}')` : `url('${desktopImg}')`;
        });
    }

    window.addEventListener('resize', updateBackgroundImages);
    updateBackgroundImages(); // Initial call to set backgrounds
});