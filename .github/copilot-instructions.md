# GitHub Copilot Instructions for olekssobol.github.io

## Project Overview
This is a personal Jekyll website hosted on GitHub Pages featuring:
- Personal portfolio & resume
- Blog posts about software development journey
- Drone video showcase (FAA Part 107 certified)
- Automated GitHub stats & commits feed
- BootDev progress tracking

## Site Structure
- **Jekyll site** with minimal-mistakes theme
- **GitHub Pages** deployment via Actions
- **Posts** in `_posts/` with YYYY-MM-DD-title.md format
- **Automated workflows** for stats updates
- **Admin panel** via Netlify CMS (`/admin/`)

## Key Files
- `_config.yml` - Jekyll configuration
- `_data/navigation.yml` - Site navigation
- `_layouts/splash.html` - Custom splash layout
- `admin/config.yml` - Netlify CMS configuration
- `scripts/` - Python automation scripts
- `_posts/` - Blog posts in Markdown

## Coding Preferences
- **Jekyll/Liquid templating** for layouts
- **GitHub Actions** for automation
- **Python scripts** for data fetching
- **Markdown** for content
- **SCSS** for styling
- **Responsive design** patterns

## Content Guidelines
- Blog posts about coding journey, projects, tutorials
- Professional tone but personal insights
- Code examples with syntax highlighting
- SEO-friendly permalinks and metadata

## When suggesting code:
1. Follow Jekyll conventions
2. Use GitHub Pages compatible gems only
3. Maintain existing design patterns
4. Consider mobile responsiveness
5. Include proper frontmatter for posts
6. Use semantic HTML and accessibility features

## Automation Workflows
- Commits feed updates via GitHub API
- BootDev progress tracking
- Project stats collection
- All run on scheduled GitHub Actions

## Deployment
- Automatic via GitHub Pages
- Custom domain: osobol.com
- HTTPS enabled
- CDN via GitHub's infrastructure