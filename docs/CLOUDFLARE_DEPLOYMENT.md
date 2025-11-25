# Deploying to Cloudflare Pages

This guide walks you through deploying your Jekyll portfolio to Cloudflare Pages.

## Prerequisites

- Cloudflare account
- GitHub repository with your Jekyll site
- Wrangler CLI (optional, for CLI deployments)

## Option 1: Deploy via Cloudflare Dashboard (Recommended)

### Step 1: Connect Your Repository

1. Log in to [Cloudflare Dashboard](https://dash.cloudflare.com/)
2. Navigate to **Pages** in the left sidebar
3. Click **Create a project**
4. Click **Connect to Git**
5. Authorize Cloudflare to access your GitHub account
6. Select your repository: `olekssobol.github.io`

### Step 2: Configure Build Settings

Set the following build configuration:

- **Production branch:** `main` (or `master`)
- **Build command:** `bundle exec jekyll build`
- **Build output directory:** `_site`

### Step 3: Environment Variables

Add these environment variables in the Cloudflare Pages dashboard:

```
RUBY_VERSION=3.2.0
JEKYLL_ENV=production
```

### Step 4: Deploy

1. Click **Save and Deploy**
2. Cloudflare will build and deploy your site
3. First deployment takes 2-5 minutes

### Step 5: Custom Domain (Optional)

1. After deployment, go to **Custom domains**
2. Add your custom domain: `osobol.com`
3. Follow DNS configuration instructions
4. Cloudflare will automatically provision SSL certificate

## Option 2: Deploy via Wrangler CLI

### Install Wrangler

```bash
npm install -g wrangler
```

### Authenticate

```bash
wrangler login
```

### Deploy

```bash
# From your project root
wrangler pages deploy _site --project-name=olekssobol-portfolio
```

**Note:** You must build the site first:

```bash
bundle exec jekyll build
```

## Build Configuration Files

### wrangler.toml

```toml
name = "olekssobol-portfolio"
compatibility_date = "2024-01-01"
pages_build_output_dir = "_site"

[site]
bucket = "_site"
```

### .cloudflare-pages.yml

```yaml
build:
  command: bundle exec jekyll build
  output_directory: _site

environment:
  RUBY_VERSION: "3.2.0"
  JEKYLL_ENV: production
```

## Continuous Deployment

Once connected to GitHub:

1. Push changes to your `main` branch
2. Cloudflare Pages automatically builds and deploys
3. Preview deployments for pull requests
4. Rollback to previous deployments anytime

## Troubleshooting

### Build Fails

**Problem:** Ruby version mismatch
**Solution:** Set `RUBY_VERSION=3.2.0` in environment variables

**Problem:** Missing dependencies
**Solution:** Ensure `Gemfile` and `Gemfile.lock` are committed

**Problem:** Jekyll build errors
**Solution:** Test locally first with `bundle exec jekyll build`

### Custom Domain Issues

**Problem:** DNS not resolving
**Solution:** Wait 24-48 hours for DNS propagation

**Problem:** SSL certificate error
**Solution:** Cloudflare auto-provisions SSL, wait 15-30 minutes

## Performance Optimizations

Cloudflare Pages includes:

- **Global CDN** - Content served from 200+ data centers
- **Automatic minification** - HTML, CSS, JS
- **Brotli compression** - Faster page loads
- **HTTP/3 support** - Latest protocol
- **DDoS protection** - Built-in security

## Migration from GitHub Pages

### DNS Changes

1. Update your DNS records from GitHub Pages to Cloudflare:

**Old (GitHub Pages):**
```
A     185.199.108.153
A     185.199.109.153
A     185.199.110.153
A     185.199.111.153
CNAME olekssobol.github.io
```

**New (Cloudflare Pages):**
```
CNAME osobol.com.pages.dev
```

Or use Cloudflare's automatic DNS configuration.

### Benefits of Cloudflare Pages

- ✅ Faster global delivery (200+ locations vs GitHub's fewer)
- ✅ Unlimited bandwidth (GitHub has soft limits)
- ✅ Better DDoS protection
- ✅ More build minutes (5000/month vs GitHub's 2000)
- ✅ Preview deployments for PRs
- ✅ Advanced analytics
- ✅ Edge functions support (if needed later)

## Rollback

If you need to rollback:

1. Go to **Deployments** in Cloudflare Pages
2. Find the working deployment
3. Click **Rollback to this deployment**

## Support

- [Cloudflare Pages Docs](https://developers.cloudflare.com/pages/)
- [Jekyll Deployment Guide](https://jekyllrb.com/docs/deployment/)
- [Wrangler CLI Docs](https://developers.cloudflare.com/workers/wrangler/)

---

**Ready to deploy?** Follow Option 1 above for the easiest setup!
