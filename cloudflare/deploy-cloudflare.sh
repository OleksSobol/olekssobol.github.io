#!/bin/bash
# Deploy to Cloudflare Pages using Wrangler CLI

set -e  # Exit on error

# Navigate to project root
cd "$(dirname "$0")/.."

echo "🚀 Deploying to Cloudflare Pages..."
echo ""

# Check if wrangler is installed
if ! command -v wrangler &> /dev/null; then
    echo "❌ Wrangler CLI not found!"
    echo "Install it with: npm install -g wrangler"
    exit 1
fi

# Check if Jekyll is installed
if ! command -v bundle &> /dev/null; then
    echo "❌ Bundler not found!"
    echo "Install it with: gem install bundler"
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
bundle install

# Build the site
echo "🔨 Building Jekyll site..."
JEKYLL_ENV=production bundle exec jekyll build

# Check if build was successful
if [ ! -d "_site" ]; then
    echo "❌ Build failed - _site directory not found"
    exit 1
fi

echo "✅ Build complete!"
echo ""

# Deploy to Cloudflare Pages
echo "☁️ Deploying to Cloudflare Pages..."
wrangler pages deploy _site --project-name=olekssobol-portfolio

echo ""
echo "✅ Deployment complete!"
echo "🌐 Your site will be available shortly at your Cloudflare Pages URL"
