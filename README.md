# Django Web Crawler

Django Web Crawler is a lightweight Django app designed to connect to websites and gather links efficiently.

## Quick Start

1. **Installation**

   Add "web_crawler" to your `INSTALLED_APPS` setting in your Django project's `settings.py` file:

   ```python
   INSTALLED_APPS = [
       # ...
       'web_crawler',
   ]
   ```
2. **Usage**

   Import the `main` module in your code:
   ```python
   from web_crawler.crawler import main
   ```
   Initialize the StartPoint class like this:
   ```python
   crawler = main.StartPoint("https://example.com", max_crawl=50, number_of_threads=10)
   ```
   ####The StartPoint class can be initialized with three arguments:
   * homepage: a positional argument of the website to gather its links.
   * max_crawl: maximum number of links to gather from the website; default is 50
   * number_of_threads: number of threads to perform the work simultaneously; default is 10
   
   After initializing the class, you can then call the "start" method like this:
   ```python
   crawler.start()
   ```
3. **Results**
   
   When the crawler has finished gathering the links, you can access the gathered links like this:
   ```python
   crawler.result
   ```
   
##Example

```python
from web_crawler.crawler import main

# Initialize the crawler
crawler = main.StartPoint("https://example.com", max_crawl=50, number_of_threads=10)

# Start crawling
crawler.start()

# Access the gathered links
links = crawler.result

# Process the links as needed
for link in links:
    print(link)
```