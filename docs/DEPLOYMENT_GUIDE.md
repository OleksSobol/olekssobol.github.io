# Complete Deployment Guide - Cloudflare Pages

## 🎯 Quick Start (Recommended Method)

### 1. Connect via Cloudflare Dashboard

This is the **easiest** and **recommended** approach:

1. Go to [Cloudflare Dashboard](https://dash.cloudflare.com/) → **Pages**
2. Click **Create a project** → **Connect to Git**
3. Select your GitHub repository: `olekssobol.github.io`
4. Configure build settings:
   - **Production branch:** `main`
   - **Build command:** `bundle exec jekyll build`
   - **Build output directory:** `_site`
5. Add environment variables:
   - `RUBY_VERSION` = `3.2.0`
   - `JEKYLL_ENV` = `production`
6. Click **Save and Deploy**

**Done!** Your site will be live in 2-5 minutes.

---

## 📋 Configuration Files

Configuration files are organized in the following directories:

### `cloudflare/` Directory
- **`wrangler.toml`** - Wrangler CLI configuration
- **`.cloudflare-pages.yml`** - Build configuration
- **`deploy-cloudflare.sh`** - Automated deployment script

### Root Directory
- **`_headers`** - HTTP headers for security and caching
- **`_redirects`** - URL redirects and 404 handling

### `docs/` Directory
- **`DEPLOYMENT_GUIDE.md`** - This guide
- **`CLOUDFLARE_DEPLOYMENT.md`** - Detailed instructions

---

## 🚀 Deployment Methods

### Method A: Dashboard (Easiest)
Follow the Quick Start above.

### Method B: Wrangler CLI

**Prerequisites:**
```bash
npm install -g wrangler
```

**Deploy:**
```bash
# Make script executable (Unix/Mac)
chmod +x cloudflare/deploy-cloudflare.sh

# Run deployment from project root
./cloudflare/deploy-cloudflare.sh
```

Or manually:
```bash
# Build
bundle exec jekyll build

# Deploy
wrangler pages deploy _site --project-name=olekssobol-portfolio
```

---

## 🔧 Custom Domain Setup

### Option 1: Using Cloudflare DNS (Recommended)

1. Transfer your domain DNS to Cloudflare (if not already)
2. In Cloudflare Pages → **Custom domains**
3. Add `osobol.com`
4. Cloudflare automatically configures DNS

### Option 2: External DNS

Add CNAME record:
```
CNAME osobol.com -> your-project.pages.dev
```

**SSL Certificate:** Auto-provisioned by Cloudflare (15-30 minutes)

---

## ⚡ Performance Features

Your site now benefits from:

- **Global CDN** - 200+ data centers worldwide
- **Automatic HTTPS** - Free SSL certificates
- **DDoS Protection** - Built-in security
- **Brotli Compression** - Faster page loads
- **HTTP/3** - Latest protocol support
- **Smart Caching** - Configured via `_headers` file

---

## 📊 Analytics Setup

Enable Web Analytics in Cloudflare Dashboard:

1. Go to **Web Analytics**
2. Add your domain
3. Copy the analytics snippet (if not auto-injected)

---

## 🔄 Continuous Deployment

**Automatic deployments:**
- Push to `main` → Auto-deploy to production
- Push to other branches → Preview deployment
- Pull requests → Preview URL in PR comments

**Preview Deployments:**
Each branch/PR gets a unique URL:
```
https://[branch].[project].pages.dev
```

---

## 📈 Monitoring

### Check Build Status
Dashboard → Pages → Your Project → Deployments

### View Build Logs
Click on any deployment to see detailed logs

### Rollback
Click **Rollback** on any previous successful deployment

---

## 🛡️ Security Headers

The `_headers` file configures:
- X-Frame-Options (prevent clickjacking)
- X-Content-Type-Options (prevent MIME sniffing)
- X-XSS-Protection (XSS protection)
- Referrer-Policy (privacy)
- Cache-Control (performance)

---

## 🔗 Redirects

The `_redirects` file handles:
- www → non-www redirect
- GitHub Pages → Custom domain redirect
- 404 error handling

**Add custom redirects:**
```
/old-path /new-path 301
```

---

## 🐛 Troubleshooting

### Build Fails

**Check Ruby version:**
```bash
# Local test
bundle exec jekyll build
```

**Set correct Ruby version:**
In Cloudflare dashboard → Environment variables:
```
RUBY_VERSION=3.2.0
```

### DNS Issues

**Check DNS propagation:**
```bash
nslookup osobol.com
```

**Wait time:** 24-48 hours for full propagation

### SSL Certificate Not Working

- Wait 15-30 minutes after adding custom domain
- Ensure DNS is correctly configured
- Check Cloudflare SSL mode is "Full" or "Full (strict)"

---

## 💡 Pro Tips

1. **Local Testing:**
   ```bash
   bundle exec jekyll serve
   # Visit http://localhost:4000
   ```

2. **Preview Before Deploy:**
   Create a branch, push, and test the preview URL

3. **Purge Cache:**
   Dashboard → Caching → Purge Everything (if needed)

4. **Environment Variables:**
   Set different variables for production vs preview branches

5. **Build Optimization:**
   Minify HTML/CSS/JS → Faster page loads

---

## 📚 Resources

- [Cloudflare Pages Docs](https://developers.cloudflare.com/pages/)
- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [Wrangler CLI Docs](https://developers.cloudflare.com/workers/wrangler/)
- [Cloudflare Support](https://support.cloudflare.com/)

---

## 🎉 Migration Checklist

- [ ] Connect GitHub repository to Cloudflare Pages
- [ ] Configure build settings
- [ ] Set environment variables
- [ ] First deployment successful
- [ ] Add custom domain
- [ ] Configure DNS
- [ ] Verify SSL certificate
- [ ] Test all pages and links
- [ ] Enable Web Analytics
- [ ] Update any external links to new domain
- [ ] Redirect old GitHub Pages URL

---

## 🆘 Need Help?

**Build issues:** Check `CLOUDFLARE_DEPLOYMENT.md` for detailed troubleshooting

**General questions:** [Cloudflare Community](https://community.cloudflare.com/)

**Email support:** Through Cloudflare dashboard

---

**Your portfolio is ready for Cloudflare Pages! 🚀**

Choose your deployment method above and get started!
