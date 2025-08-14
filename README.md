# 🦉 owl-webmap

**owl-webmap** is a simple Python tool that parses and displays information from a website’s `robots.txt` and `sitemap.xml` files.  
This is useful for reconnaissance, SEO analysis, and discovering hidden or disallowed paths.

Created by **KHALED.S.HADDAD**  
🌐 [https://khaledhaddad.tech](https://khaledhaddad.tech)

---

## 🌐 Features

- 🔍 Fetches and parses `/robots.txt`
  - Extracts and displays all `Disallow:` rules
- 🗺️ Fetches and parses `/sitemap.xml`
  - Lists all URLs found in the sitemap
- 🧭 Automatically prepends `http://` if scheme is missing
- ⚡ Lightweight and fast

---

## 🛠️ Requirements

- Python 3.x
- Required libraries:

```bash
pip install requests beautifulsoup4

