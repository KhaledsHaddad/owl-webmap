#!/usr/bin/env python3
import sys
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def fetch_robots(domain):
    url = urljoin(domain, "/robots.txt")
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.text.splitlines()
    except:
        pass
    return []

def fetch_sitemap(domain):
    url = urljoin(domain, "/sitemap.xml")
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.text
    except:
        pass
    return None

def parse_robots(lines):
    disallowed = []
    for line in lines:
        if line.strip().lower().startswith("disallow:"):
            path = line.split(":")[1].strip()
            if path:
                disallowed.append(path)
    return disallowed

def parse_sitemap(xml):
    soup = BeautifulSoup(xml, "xml")
    return [loc.text for loc in soup.find_all("loc")]

def main():
    if len(sys.argv) != 2:
        print("Usage: owl-webmap <url>")
        sys.exit(1)

    domain = sys.argv[1]
    if not domain.startswith("http"):
        domain = "http://" + domain

    print(f"Fetching robots.txt from {domain}")
    robots_lines = fetch_robots(domain)
    disallowed = parse_robots(robots_lines)
    if disallowed:
        print("Disallowed paths:")
        for path in disallowed:
            print(f" - {urljoin(domain, path)}")
    else:
        print("No disallowed paths found.")
    print()

    print(f"Fetching sitemap.xml from {domain}")
    sitemap_xml = fetch_sitemap(domain)
    if sitemap_xml:
        urls = parse_sitemap(sitemap_xml)
        if urls:
            print("Sitemap URLs:")
            for u in urls:
                print(f" - {u}")
        else:
            print("No URLs found in sitemap.")
    else:
        print("Sitemap not found.")

if __name__ == "__main__":
    main()
