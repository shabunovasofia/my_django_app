const sidebar = document.getElementById('sidebar');
const menuToggle = document.getElementById('menuToggle');

sidebar.addEventListener('mouseenter', () => {
    if (window.innerWidth > 768) {
        sidebar.classList.add('active');
    }
});

sidebar.addEventListener('mouseleave', () => {
    if (window.innerWidth > 768) {
        sidebar.classList.remove('active');
    }
});
