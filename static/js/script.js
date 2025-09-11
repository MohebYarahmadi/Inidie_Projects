// Mobile menu toggle
document.getElementById('mobile-menu-toggle').addEventListener('click', function() {
    document.getElementById('nav-menu').classList.toggle('show');
});

// Filter buttons for showcase page
if (document.querySelector('.filter-btn')) {
    const filterButtons = document.querySelectorAll('.filter-btn');
    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            filterButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
        });
    });
}
