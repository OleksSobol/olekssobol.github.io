# Portfolio Structure Guide

This document explains the organization of the portfolio website.

## Directory Structure

### 📁 Configuration & Deployment

#### `cloudflare/`
Cloudflare Pages deployment configuration
- `wrangler.toml` - Wrangler CLI config
- `.cloudflare-pages.yml` - Build settings
- `deploy-cloudflare.sh` - Deployment script
- `README.md` - Deployment quick reference

#### `docs/`
Documentation and guides
- `DEPLOYMENT_GUIDE.md` - Quick start guide
- `CLOUDFLARE_DEPLOYMENT.md` - Detailed instructions
- `README.md` - Documentation index

---

### 📄 Content

#### `_pages/`
All website content pages (organized to keep root clean)
- `about.md` - About page
- `projects.md` - Projects showcase
- `playground.md` - Interactive tools
- `videos.md` - Drone portfolio
- `blog.md` - Blog index
- `contact.md` - Contact page
- `commits.md` - GitHub commits
- `post.md` - Post template

#### `_posts/`
Blog posts (Markdown files with YAML front matter)
- Format: `YYYY-MM-DD-title.md`

#### `index.md`
Homepage (only content page in root for convention)

---

### 🎨 Assets & Design

#### `assets/`
Static files
- `images/` - Images, photos, screenshots
- `css/` - Custom stylesheets
- `js/` - JavaScript files
- `resume.pdf` - Downloadable resume

#### `_layouts/`
Custom Jekyll layouts

---

### ⚙️ Configuration Files

#### Root Configuration
- `_config.yml` - Main Jekyll configuration
- `_headers` - HTTP security & caching headers (Cloudflare)
- `_redirects` - URL redirects (Cloudflare)
- `Gemfile` - Ruby dependencies
- `.gitignore` - Git ignore rules
- `CNAME` - Custom domain configuration

#### `_data/`
Site data files
- `navigation.yml` - Navigation menu structure
- `bootdev.json` - Boot.dev stats (auto-updated)

---

### 🛠️ Utilities

#### `scripts/`
Build and automation scripts

#### `admin/`
Netlify CMS configuration (if used)

#### `.github/`
GitHub Actions workflows
- Auto-update Boot.dev stats
- Auto-update commit history
- Jekyll deployment

---

## File Organization Philosophy

### Root Directory
**Keep minimal** - Only essential config files and homepage
- Configuration files (_config.yml, Gemfile, etc.)
- One content file (index.md)
- README.md

### Subdirectories
**Organized by purpose**:
- Content → `_pages/`
- Blog → `_posts/`
- Config → `cloudflare/`, `_data/`
- Docs → `docs/`
- Assets → `assets/`

### Benefits
1. **Clean Root** - Easy to navigate
2. **Logical Grouping** - Related files together
3. **Scalable** - Easy to add new content
4. **Professional** - Industry-standard structure
5. **Maintainable** - Clear organization

---

## Adding New Content

### New Page
```bash
# Create in _pages/
touch _pages/new-page.md

# Add front matter
---
layout: single
title: "New Page"
permalink: /new-page/
---

# Add to navigation (optional)
# Edit _data/navigation.yml
```

### New Blog Post
```bash
# Create in _posts/
touch _posts/2024-11-24-my-post.md

# Add front matter
---
layout: single
title: "My Post"
date: 2024-11-24
---
```

### New Asset
```bash
# Add to assets/
cp image.png assets/images/
```

---

## Quick Reference

### Local Development
```bash
bundle exec jekyll serve
# Visit http://localhost:4000
```

### Build
```bash
bundle exec jekyll build
# Output: _site/
```

### Deploy
```bash
./cloudflare/deploy-cloudflare.sh
```

### Documentation
- Quick Start: `docs/DEPLOYMENT_GUIDE.md`
- Detailed: `docs/CLOUDFLARE_DEPLOYMENT.md`
- Cloudflare: `cloudflare/README.md`
- Pages: `_pages/README.md`

---

## Navigation Flow

```
User visits osobol.com
    ↓
index.md (Homepage)
    ↓
Navigation Menu (_data/navigation.yml)
    ├── Projects → _pages/projects.md
    ├── Playground → _pages/playground.md
    ├── Videos → _pages/videos.md
    ├── Blog → _pages/blog.md → _posts/*.md
    ├── About → _pages/about.md
    └── Contact → _pages/contact.md
```

---

**Last Updated:** 2024-11-24

This structure ensures clean organization, easy maintenance, and professional presentation.
