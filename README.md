# Worlds with You

The public information website for Worlds with You, an interactive fiction product in development by Exoself Systems.

**Website:** https://worldswithyou.com · **Contact:** info@worldswithyou.com

## Development

The site uses semantic HTML, CSS, and locally served artwork. It has no JavaScript runtime, third-party tracking, web fonts, package dependencies, or application backend. Python 3.9+ runs the build and link checks.

```sh
just serve   # Local preview: http://127.0.0.1:4173
just check   # Check page metadata, links, anchors, and assets
just build   # Validate and copy public/ to _site/
```

Edit files under `public/`. Every push to `main` validates and deploys `_site/` through GitHub Actions to GitHub Pages. The workflow uses commit-pinned official GitHub actions. GitHub supplies the deployment token; no repository secrets are required.

## Domain

The intended custom domain is `worldswithyou.com`. GitHub Pages Settings must also contain that domain: with an Actions deployment, the `CNAME` file alone does not configure it.

At the DNS provider, create four A records for `@`: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, and `185.199.111.153`. Add `www` as a CNAME pointing to `kavinstewart.github.io`. Remove conflicting website records only. Keep email and verification records.

Once DNS resolves correctly and GitHub issues the certificate, enable **Enforce HTTPS** in repository Settings → Pages. Verify the domain in GitHub account Settings → Pages to protect its ownership.

Sources: [GitHub custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site), [Namecheap GitHub Pages guide](https://www.namecheap.com/support/knowledgebase/article.aspx/9645/2208/how-do-i-link-my-domain-to-github-pages/).

## Content and scope

The website describes a product in development. It makes no claims about funding, incorporation dates, customer numbers, revenue, launch dates, or startup-program acceptance. `public/privacy/` and `public/terms/` publish the Worlds with You app privacy policy and terms of service, which also cover this website. Their source of truth is `docs/legal/` in the private product repository; edit them there and regenerate these pages. Revisit them if the website adds forms, analytics, or accounts.

Original artwork provenance is recorded in `ASSETS.md`. This public repository contains only the marketing website; product source and internal company documents are not part of it.
