# Personal Website Rebuild Guide

## Overview

Your personal website is now rebuilt with a **Neo Hacker** theme - clean, modern, fast, with subtle hacker vibes but polished. Built on Jekyll + Minimal Mistakes, deployed on GitHub Pages.

**Live Site**: https://olekssobol.github.io
**Theme**: Dark with neon accents (#5cffd6)
**Vibe**: "I code at 2 AM but I do it well"

---

## Site Structure

```
olekssobol.github.io/
├── _config.yml           # Main configuration
├── index.md              # Homepage
├── _pages/               # Static pages
│   ├── about.md
│   ├── blog.md
│   ├── projects.md
│   └── playground.md
├── _posts/               # Blog posts
│   └── YYYY-MM-DD-title.md
├── _projects/            # Project case studies
│   └── project-name.md
├── _playground/          # Experiments & tools
│   └── experiment-name.md
├── _data/
│   └── navigation.yml    # Site navigation
└── assets/
    ├── css/
    │   └── main.scss     # Custom Neo Hacker theme
    └── images/
```

---

## Design Language

### Color Palette

```css
Background: #0d0d0d (primary), #1a1a1a (secondary), #2d2d2d (tertiary)
Accent: #5cffd6 (primary), #52adc8 (secondary)
Text: #e2e2e2 (primary), #b0b0b0 (secondary), #6a6a6a (muted)
Borders: #3a3a3a
Code Background: #1e1e1e
```

### Typography

- **Body Text**: Inter (clean, readable)
- **Headings**: JetBrains Mono (monospace, hacker vibes)
- **Code**: JetBrains Mono

### Design Principles

- Dark theme, minimal colors
- Sharp typography
- No corporate nonsense
- Fast loading
- Mobile-friendly
- Clean, not cluttered

---

## Navigation

Current structure (defined in `_data/navigation.yml`):

1. **Home** - Landing page with intro and featured projects
2. **Projects** - Case studies and portfolio items
3. **Blog** - Technical posts and notes
4. **Playground** - Experiments and tools
5. **About** - Personal story and background

---

## Content Sections

### 1. Home (`/`)

**Purpose**: First impression, show don't tell

**Content**:
- Punchy headline
- Tech stack badges
- 3 featured projects
- Latest blog posts
- Current learning section
- CTA buttons

**Tone**: Direct, confident, no fluff

### 2. Projects (`/projects/`)

**Purpose**: Portfolio and case studies

**Content Format**:
- TL;DR at top
- Problem → Solution breakdown
- Technical stack
- Results with numbers
- Links to code/demo

**Template**: `_projects/example-project.md`

**Existing Projects**:
- Utopia Account Creation (UAC)
- DHCP Lease Runner (DLR)
- Expense Tracker
- Wedding Website
- Various learning projects

### 3. Blog (`/blog/`)

**Purpose**: Technical notes and lessons learned

**Categories**:
- **Engineering** - Backend systems, APIs, architecture
- **Notes** - Quick fixes, snippets, TIL moments
- **Experiments** - Random hacks and explorations
- **Career** - Learning paths and growth

**Template**: `_posts/TEMPLATE-blog-post.md`

**Naming**: `YYYY-MM-DD-title-with-hyphens.md`

### 4. Playground (`/playground/`)

**Purpose**: Interactive tools and experiments

**Current Tools**:
- API Tester
- JSON Formatter
- Base64 Encoder/Decoder
- URL Encoder
- Subnet Calculator
- UUID Generator

**Template**: `_playground/example-experiment.md`

**Vibe**: "Sometimes useful. Always educational."

### 5. About (`/about/`)

**Purpose**: Personal story, not LinkedIn bio

**Content**:
- Journey from network engineer to developer
- Impact metrics
- Tech skills (visual, not boring lists)
- What makes you different
- Current learning
- Contact info

**Tone**: Human, honest, no corporate speak

---

## Creating New Content

### New Blog Post

```bash
# Create file
touch _posts/2025-11-30-your-post-title.md
```

```yaml
---
title: "Your Post Title"
date: 2025-11-30
categories:
  - engineering
tags:
  - python
  - api
excerpt: "One-sentence summary"
toc: true
toc_sticky: true
---

## Your Content Here
```

### New Project

```bash
# Create file
touch _projects/project-name.md
```

```yaml
---
title: "Project Name"
excerpt: "Brief description"
date: 2025-11-30
categories:
  - automation
tags:
  - python
  - docker
---

## Your Project Details
```

### New Playground Item

```bash
# Create file
touch _playground/experiment-name.md
```

```yaml
---
title: "Experiment Name"
excerpt: "What it does"
date: 2025-11-30
tags:
  - automation
---

## Your Experiment
```

---

## Local Development

### Build & Serve Locally

```bash
# Install dependencies (first time only)
bundle install

# Serve site locally
bundle exec jekyll serve

# Open browser to:
# http://localhost:4000
```

### Live Reload

The local server auto-reloads on file changes. Just save and refresh.

---

## Deployment

### GitHub Pages (Automatic)

1. Push to `main` branch
2. GitHub Actions builds automatically
3. Live in ~2-5 minutes

### Manual Check

```bash
# Build site
bundle exec jekyll build

# Check _site/ directory for output
ls -la _site/
```

---

## Customization

### Change Colors

Edit `assets/css/main.scss`:

```scss
:root {
  --accent-primary: #5cffd6;  // Change this
  --accent-secondary: #52adc8; // And this
}
```

### Change Navigation

Edit `_data/navigation.yml`:

```yaml
main:
  - title: "New Page"
    url: /new-page/
```

### Add New Section

1. Create new collection in `_config.yml`
2. Create `_collection-name/` directory
3. Add navigation link
4. Create landing page in `_pages/`

---

## Plugins & Features

### Active Plugins

- `jekyll-include-cache` - Performance
- `jekyll-paginate` - Blog pagination
- `jekyll-feed` - RSS feed
- `jekyll-seo-tag` - SEO optimization
- `jekyll-sitemap` - Sitemap generation

### Features Enabled

- Search (full content)
- Reading time
- Table of contents
- Social sharing
- Related posts
- Categories & tags
- Code syntax highlighting

---

## Performance

### Optimizations

- Minimal CSS (single file)
- No JavaScript dependencies (except Playground)
- Lazy image loading
- Compressed HTML
- Fast Google Fonts loading

### Monitoring

Check performance:
- Google PageSpeed Insights
- GTmetrix
- WebPageTest

---

## Content Guidelines

### Writing Tone

**DO**:
- Be direct and honest
- Use "I" not "we"
- Show results with numbers
- Keep it real
- Technical but accessible

**DON'T**:
- Corporate buzzwords
- Excessive jargon
- "Passionate self-motivated..."
- Over-promising
- Boring technical dumps

### Headlines

Good: "Building a FastAPI service that handles 10k req/sec"
Bad: "My Journey with Modern Backend Development"

Good: "How I cut deployment time from 2 hours to 5 minutes"
Bad: "Exploring DevOps Best Practices"

### Code Examples

- Always include context
- Add comments for clarity
- Show real code, not pseudocode
- Explain why, not just what

---

## Maintenance

### Regular Updates

- Update resume PDF when needed
- Add new projects as you build them
- Blog when you solve interesting problems
- Keep tech stack badges current
- Update learning progress

### Content Calendar Ideas

- Technical deep dives (monthly)
- Quick tips and TILs (weekly)
- Project retrospectives (as completed)
- Career updates (quarterly)

---

## Branding

### Your Brand Identity

**Who you are**:
- Backend engineer who automates chaos
- System builder, not resume polisher
- Technical but pragmatic
- Learning-focused

**Vibe**:
- "I build things because it's fun and sometimes chaos"
- Clean but not corporate
- Technical but not pretentious
- Playful but not unprofessional

### Voice & Tone

- **Confident** but not arrogant
- **Technical** but accessible
- **Direct** not verbose
- **Honest** about wins and failures

---

## Common Tasks

### Update Featured Projects (Homepage)

Edit `index.md`, change the project cards:

```markdown
<a href="/projects/new-project/" class="project-card">
  <div class="project-title">New Project</div>
  <div class="project-desc">Description here</div>
</a>
```

### Add Tech Badge

```html
<span class="tech-badge">New Tech</span>
```

### Change Bio

Edit `_config.yml`:

```yaml
author:
  bio: "New bio here"
```

### Update Contact Info

Edit `_pages/about.md` in the Connect section

---

## Troubleshooting

### Site Not Building

```bash
# Check build errors
bundle exec jekyll build --verbose

# Common issues:
# - YAML front matter errors
# - Missing required fields
# - Incorrect date format
```

### CSS Not Loading

```bash
# Clear Jekyll cache
bundle exec jekyll clean

# Rebuild
bundle exec jekyll serve
```

### Images Not Showing

- Check path (use `/assets/images/file.png`)
- Verify file exists
- Check file extension case

---

## Next Steps

### Immediate Priorities

1. Update resume PDF
2. Add real project pages for UAC and DLR
3. Write first technical blog post
4. Add avatar image
5. Create 2-3 playground experiments

### Future Enhancements

- Comments (Giscus integration)
- Analytics (privacy-friendly)
- Newsletter signup
- Dark/light mode toggle
- More playground tools
- Video embeds for drone footage

---

## Resources

### Documentation

- [Jekyll Docs](https://jekyllrb.com/docs/)
- [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/)
- [GitHub Pages](https://docs.github.com/en/pages)

### Inspiration

- [Dan Abramov](https://overreacted.io/)
- [Julia Evans](https://jvns.ca/)
- [Xe Iaso](https://xeiaso.net/)

### Tools

- [Carbon](https://carbon.now.sh/) - Code screenshots
- [Excalidraw](https://excalidraw.com/) - Diagrams
- [Unsplash](https://unsplash.com/) - Free images

---

## Support

If something breaks:

1. Check GitHub Actions build logs
2. Test locally with `bundle exec jekyll serve`
3. Review recent changes
4. Check Jekyll/Minimal Mistakes docs
5. Search GitHub issues

---

**Built with**: Jekyll + Minimal Mistakes
**Deployed on**: GitHub Pages
**Theme**: Neo Hacker (Custom)
**Last Updated**: November 2025

Keep it real. Keep it technical. Keep shipping.
