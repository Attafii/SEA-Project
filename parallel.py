import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import time
import threading

# Shared variables
urls = [f'https://en.wikipedia.org/wiki/Special:Random' for _ in range(500)]
results = []
progress_counter = 0
results_lock = threading.Lock()
num_threads = 50  # Number of threads

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

def worker(urls_chunk):
    global progress_counter
    local_results = []
    for url in urls_chunk:
        result = scrape_article(url)
        if result[0]:  # Check if the article was successfully scraped
            local_results.append(result)
            with results_lock:
                progress_counter += 1
    with results_lock:
        results.extend(local_results)

def partition_urls(urls, num_threads):
    avg_chunk_size = len(urls) // num_threads
    partitions = [urls[i:i + avg_chunk_size] for i in range(0, len(urls), avg_chunk_size)]
    return partitions

start_time = time.time()  # Start timing

# Partition the URLs into chunks
url_partitions = partition_urls(urls, num_threads)

# Start the ThreadPoolExecutor with thread partitioning
with ThreadPoolExecutor(max_workers=num_threads) as executor:
    executor.map(worker, url_partitions)

# Print results and progress
for title, first_paragraph, links in results:
    print(f'Title: {title}')
    print(f'First Paragraph: {first_paragraph[:100]}...')  # Print only the first 100 characters for brevity
    print(f'Links: {links[:5]}')  # Print only the first 5 links for brevity

end_time = time.time()  # End timing
print(f"Parallel scraping took {end_time - start_time:.2f} seconds.")
print(f"Total progress: {progress_counter}/{len(urls)}")