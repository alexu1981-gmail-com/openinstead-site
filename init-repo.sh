#!/bin/bash
# Init local git repo + push to GitHub.
# Usage: ./init-repo.sh YOUR_GITHUB_USERNAME REPO_NAME
# Example: ./init-repo.sh alexu1981 openinstead-site
#
# Before running:
# 1. Create an EMPTY repo on github.com with the given REPO_NAME.
#    Do NOT initialize with README / .gitignore / license — leave it empty.
# 2. Make sure `git` is installed (`git --version`). On macOS: `xcode-select --install`.

set -e

if [ $# -lt 2 ]; then
  echo "Usage: $0 <github_username> <repo_name>"
  echo "Example: $0 alexu1981 openinstead-site"
  exit 1
fi

GH_USER="$1"
REPO_NAME="$2"

cd "$(dirname "$0")"

echo "==> Cleaning any partial .git directory"
rm -rf .git

echo "==> Initializing fresh git repo"
git init -b main
git config user.email "alexu1981@gmail.com"
git config user.name "Alexandru"

echo "==> Staging files"
git add -A

echo "==> First commit"
git commit -m "Initial commit: OpenInstead pSEO site (257 pages)

- 44 SaaS products mapped to 68 OSS alternatives
- 121 side-by-side comparison pages
- 20 categories
- Build: pip install pyyaml jinja2 && python3 build.py
- Deploy: Cloudflare Pages or Netlify (static site, dist/)"

echo "==> Adding GitHub remote"
git remote add origin "https://github.com/${GH_USER}/${REPO_NAME}.git"

echo "==> Pushing to GitHub"
git push -u origin main

echo ""
echo "Done. Your code is now at https://github.com/${GH_USER}/${REPO_NAME}"
echo "Next: connect this repo to Cloudflare Pages (see DEPLOY_NOW.md)"
