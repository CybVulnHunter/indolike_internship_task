import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

def get_url():
    url = input("Enter the URL (including http/https): ")
    if not url.startswith(('http://', 'https://')):
        print("Invalid URL format. Make sure to include http:// or https://")
        return None
    return url

def fetch_html(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return None

def extract_links(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    js_files, php_files, html_files, urls = set(), set(), set(), set()

    for tag in soup.find_all(['script', 'a', 'link']):
        link = tag.get('src') or tag.get('href')
        if link:
            full_url = urljoin(base_url, link)
            if link.endswith('.js'):
                js_files.add(full_url)
            elif link.endswith('.php'):
                php_files.add(full_url)
            elif link.endswith('.html'):
                html_files.add(full_url)
            else:
                urls.add(full_url)

    return js_files, php_files, html_files, urls

def scrape_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    headings = [h.get_text(strip=True) for h in soup.find_all(['h1', 'h2', 'h3'])]
    paragraphs = [p.get_text(strip=True) for p in soup.find_all('p')]
    return headings, paragraphs

def main():
    url = get_url()
    if not url:
        return

    html = fetch_html(url)
    if not html:
        return

    js_files, php_files, html_files, urls = extract_links(html, url)
    headings, paragraphs = scrape_data(html)

    print("\n[+] JavaScript Files Found:")
    print('\n'.join(js_files) if js_files else "None")

    print("\n[+] PHP Files Found:")
    print('\n'.join(php_files) if php_files else "None")

    print("\n[+] HTML Files Found:")
    print('\n'.join(html_files) if html_files else "None")

    print("\n[+] Other URLs Found:")
    print('\n'.join(urls) if urls else "None")

    print("\n[+] Scraped Data:")
    print("Headings:", headings if headings else "None")
    print("Paragraphs:", paragraphs[:5] if paragraphs else "None")  # Limiting to 5 paragraphs

if __name__ == "__main__":
    main()
