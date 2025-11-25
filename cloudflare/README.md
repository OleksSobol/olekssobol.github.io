# Cloudflare Pages Configuration

This folder contains all configuration files for deploying to Cloudflare Pages.

## Files

- **`wrangler.toml`** - Wrangler CLI configuration
- **`.cloudflare-pages.yml`** - Build settings for Cloudflare Pages
- **`deploy-cloudflare.sh`** - Automated deployment script

## Quick Deploy

### Via Dashboard (Recommended)
See `../docs/DEPLOYMENT_GUIDE.md`

### Via CLI
```bash
# From project root
./cloudflare/deploy-cloudflare.sh
```

Or manually:
```bash
# Install Wrangler
npm install -g wrangler

# Login
wrangler login

# Build site
bundle exec jekyll build

# Deploy
wrangler pages deploy _site --project-name=olekssobol-portfolio
```

## Documentation

Full deployment instructions are in:
- **Quick Start:** `docs/DEPLOYMENT_GUIDE.md`
- **Detailed Guide:** `docs/CLOUDFLARE_DEPLOYMENT.md`
