import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import time

# Generate a list of 500 Wikipedia article URLs
urls = [f'https://en.wikipedia.org/wiki/Special:Random' for _ in range(500)]

def scrape_article(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extracting the title
        title = soup.find('h1', {'id': 'firstHeading'}).text
        
        # Extracting the first paragraph
        first_paragraph = soup.find('p').text
        
        # Extracting links to other Wikipedia pages
        links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith('/wiki/')]

        return title, first_paragraph, links
    except Exception as e:
        return None, None, None  # Handle errors gracefully

start_time = time.time()  # Start timing

with ThreadPoolExecutor(max_workers=30) as executor:  # Increased number of workers for better parallelism
    results = list(executor.map(scrape_article, urls))

for title, first_paragraph, links in results:
    if title:  # Check if the article was successfully scraped
        print(f'Title: {title}')
        print(f'First Paragraph: {first_paragraph[:100]}...')  # Print only the first 100 characters for brevity
        print(f'Links: {links[:5]}')  # Print only the first 5 links for brevity

end_time = time.time()  # End timing
print(f"Parallel scraping took {end_time - start_time:.2f} seconds.")
