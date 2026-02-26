// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Active nav link highlighting on scroll
const sections = document.querySelectorAll('section');
const navLinks = document.querySelectorAll('nav a');

window.addEventListener('scroll', () => {
    let current = '';
    
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        
        if (scrollY >= sectionTop - 200) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href').slice(1) === current) {
            link.classList.add('active');
        }
    });
});

// Add more interactive features as needed
// Theme toggle: toggles `body.light-theme`, updates icon, and persists preference
(function() {
    const themeToggleBtn = document.getElementById('theme-toggle');
    const themeLabel = themeToggleBtn ? themeToggleBtn.querySelector('.theme-label') : null;

    function applyTheme(isLight) {
        if (isLight) document.body.classList.add('light-theme');
        else document.body.classList.remove('light-theme');

        // Button shows the target theme (what will be applied on click)
        if (themeLabel) themeLabel.textContent = isLight ? 'Dark' : 'Light';
        if (themeToggleBtn) {
            themeToggleBtn.setAttribute('aria-pressed', isLight ? 'true' : 'false');
            themeToggleBtn.setAttribute('aria-label', isLight ? 'Switch to Dark theme' : 'Switch to Light theme');
        }
    }

    if (!themeToggleBtn) return console.log('No theme toggle button found');

    // Initialize from localStorage or system preference
    const stored = localStorage.getItem('theme');
    if (stored === 'light') applyTheme(true);
    else if (stored === 'dark') applyTheme(false);
    else {
        const prefersLight = window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches;
        applyTheme(prefersLight);
    }

    themeToggleBtn.addEventListener('click', () => {
        const isLight = document.body.classList.toggle('light-theme');
        applyTheme(isLight);
        localStorage.setItem('theme', isLight ? 'light' : 'dark');
        themeToggleBtn.classList.add('toggled');
        setTimeout(() => themeToggleBtn.classList.remove('toggled'), 250);
    });
})();

console.log('Portfolio script loaded successfully');
