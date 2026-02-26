# Portfolio Website

A modern, dark-themed portfolio website built with vanilla HTML, CSS, and JavaScript.

## Project Structure

```
Portfolio/
├── index.html      # Main HTML file with page structure
├── styles.css      # All styling and responsive design
├── script.js       # JavaScript for interactivity
└── README.md       # This file
```

## Technologies Used

- **HTML5** - Semantic markup and structure
- **CSS3** - Styling, animations, and responsive design
- **Vanilla JavaScript** - DOM manipulation and smooth interactions
- **No frameworks or libraries** - Pure front-end tech stack

## File Breakdown

### index.html
- **Navigation header** with sticky positioning
- **Hero section** with call-to-action button
- **Projects section** with responsive grid layout (3 project cards)
- **About section** with language proficiency info
- **Contact section** with social links
- **Footer** with copyright info

### styles.css
- **Dark color scheme**: Navy blues (#0a0e27, #0f1429, #1a1f3a) with cyan accents (#00d4ff)
- **Responsive design**: Mobile-first approach with breakpoints at 768px and 480px
- **Animations**:
  - `fadeInDown` - Hero title slides down on load
  - `fadeInUp` - Hero subtitle and CTA button slide up with stagger
- **Key features**:
  - Sticky navigation with bottom border
  - Hover effects on project cards (lift and glow)
  - Cyan accent color for all interactive elements
  - Responsive grid layout for projects (auto-fit, minmax)
  - Smooth transitions on all interactive elements

### script.js
- **Smooth scrolling**: Navigation links scroll smoothly to sections
- **Active nav highlighting**: Links highlight with cyan color as you scroll to their section
- **Scroll margin**: Sections have top margin to prevent overlap with sticky header

## Color Palette

| Color | Hex | Usage |
|-------|-----|-------|
| Dark Background | #0a0e27 | Main page background |
| Dark Navy | #0f1429 | Header, contact, footer |
| Card Background | #1a1f3a | Project cards, content containers |
| Cyan Accent | #00d4ff | Links, headings, highlights |
| Light Text | #e0e0e0 | Primary text |
| Medium Gray | #a0a0a0 | Secondary text |
| Very Dark | #050a17 | Footer |

## Key Features

1. **Sticky Navigation** - Header stays at top while scrolling
2. **Responsive Grid** - Projects layout adapts to screen size
3. **Hover Effects** - Cards lift and glow on hover
4. **Smooth Navigation** - Clicking nav links scrolls smoothly to sections
5. **Active State** - Current section is highlighted in navigation
6. **Dark Mode** - Modern dark theme with high contrast
7. **Languages Section** - Shows fluency in multiple languages
8. **Mobile Optimized** - Works great on all device sizes

## Customization Tips

### Change colors
- All color values are in `styles.css`
- Primary accent: Replace `#00d4ff` throughout
- Background: Change `#0a0e27` for main background

### Update content
- Edit text in `index.html` sections
- Change "Your Name" in the header and footer
- Add/remove project cards by duplicating/removing `.project-card` divs
- Update contact links with your actual email, GitHub, LinkedIn, etc.

### Add more projects
- Copy a `.project-card` div
- Paste it in the `.project-grid`
- Update title, description, and tags

### Modify animations
- Find `@keyframes` in `styles.css` to adjust animations
- Change `animation` properties on elements to modify duration/delay

## Responsive Breakpoints

- **768px and below**: Adjusted font sizes, gap spacing, direction changes
- **480px and below**: Single column layouts, smaller fonts, compact navigation

## Reusable Across Pages

The `styles.css` and `script.js` files are designed to be reusable across multiple pages in your portfolio project. Both files use semantic class names that won't conflict with other pages.

## Future Enhancements

Ideas to expand this portfolio:
- Add a Skills section with technical proficiency
- Implement dark/light mode toggle
- Create a Contact form with validation
- Add project images/screenshots
- Implement lazy loading for images
- Add testimonials carousel
- Create sub-pages for individual projects
- Add a blog section
- Implement filtering for projects by technology

## Notes

- No external dependencies required
- Lightweight and fast loading
- SEO-friendly HTML structure
- Mobile-first design approach
- All animations use CSS3 for performance
