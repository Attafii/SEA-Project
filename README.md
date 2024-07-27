# Web Scraping Performance Comparison

This repository contains a Python project for comparing the performance of sequential and parallel web scraping techniques. The project scrapes data from 500 Wikipedia URLs to demonstrate the differences in execution time and efficiency between the two methods.

## Project Overview

The project includes two Python scripts:

1. **`sequential_.py`**: Scrapes data sequentially from 500 Wikipedia URLs.
2. **`parallel.py`**: Scrapes data in parallel using multiple threads from 500 Wikipedia URLs.

Both scripts perform the same scraping task but use different approaches to handle multiple URLs. The goal is to observe and compare the time taken by each method and assess their performance.

## Visual Representation

Here is a diagram illustrating the difference between sequential and parallel scraping:

![Web Scraping Diagram](https://github.com/Attafii/SEA-Project/blob/master/example.png)

## Features

- **Sequential Scraping**: Executes requests one at a time.
- **Parallel Scraping**: Uses `ThreadPoolExecutor` to execute requests concurrently.
- **Error Handling**: Logs errors and exceptions for better debugging.
- **Performance Metrics**: Measures and logs execution time for both methods.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `concurrent.futures` library (included in Python 3.2+)
- `logging` library (included in Python)

You can install the required libraries using pip:

```bash
pip install requests beautifulsoup4
