document.addEventListener("DOMContentLoaded", function() {
    const menuToggle = document.getElementById("menu-toggle");
    const nav = document.getElementById("main-nav");
    
    menuToggle.addEventListener("click", function() {
        nav.classList.toggle("show");
    });
    
    // Close nav when clicking outside
    document.addEventListener("click", function(event) {
        if (!nav.contains(event.target) && event.target !== menuToggle) {
            nav.classList.remove("show");
        }
    });
});