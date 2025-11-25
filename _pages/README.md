# Content Pages

This directory contains all the main content pages for the website.

## Pages

### Main Pages
- **`about.md`** - About page with professional background and journey
- **`projects.md`** - Project showcase with stats and tech stacks
- **`playground.md`** - Interactive developer tools (6 tools)
- **`videos.md`** - Aerial drone cinematography portfolio
- **`contact.md`** - Contact information and form

### Utility Pages
- **`blog.md`** - Blog index page
- **`commits.md`** - Latest GitHub commits page
- **`post.md`** - Blog post template/layout

## Organization

All content pages are organized in the `_pages/` directory to keep the root clean. Jekyll is configured to process these pages via `_config.yml`:

```yaml
include:
  - _pages

collections:
  pages:
    output: true
    permalink: /:title/
```

## Adding New Pages

To add a new page:

1. Create `new-page.md` in this directory
2. Add front matter:
   ```yaml
   ---
   layout: single
   title: "Page Title"
   permalink: /page-url/
   ---
   ```
3. Add to navigation in `_data/navigation.yml` if needed

## Permalinks

Each page uses a custom permalink defined in its front matter:
- `/about/` - About page
- `/projects/` - Projects page
- `/playground/` - Playground tools
- `/videos/` - Drone videos
- `/blog/` - Blog index
- `/contact/` - Contact page
