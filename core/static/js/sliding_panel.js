document.addEventListener('DOMContentLoaded', function() {
    const serviceAreaMenu = document.querySelector('.service-area-menu a');
    const quickLinksMenu = document.querySelector('.quick-links-menu a');
    const closeButtons = document.querySelectorAll('.close-button');

    if (serviceAreaMenu) {
        serviceAreaMenu.addEventListener('click', function(event) {
            event.preventDefault();
            const panel = document.getElementById('service-area-panel');
            panel.classList.toggle('open');
        });
    }

    if (quickLinksMenu) {
        quickLinksMenu.addEventListener('click', function(event) {
            event.preventDefault();
            const panel = document.getElementById('quick-links-panel');
            panel.classList.toggle('open');
        });
    }

    closeButtons.forEach(button => {
        button.addEventListener('click', function() {
            const panel = this.closest('.sliding-panel');
            panel.classList.remove('open');
        });
    });
});
