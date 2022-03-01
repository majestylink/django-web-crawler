import threading
from queue import Queue
from .spider import Spider
from .domain import *


class StartPoint:
    queue = Queue()
    result = set()
    MAX_CRAWL = int()

    def __init__(self, homepage, max_crawl=50, number_of_threads=10):
        self.HOMEPAGE = homepage
        self.DOMAIN_NAME = get_domain_name(self.HOMEPAGE)
        self.NUMBER_Of_THREADS = number_of_threads
        StartPoint.MAX_CRAWL = max_crawl

        Spider(self.DOMAIN_NAME, self.HOMEPAGE, self.DOMAIN_NAME)

    # Each worker threads (will die when main exits)
    def create_workers(self):
        for _ in range(self.NUMBER_Of_THREADS):
            t = threading.Thread(target=self.work)
            t.daemon = True
            t.start()

    # Do the next job in the queue
    def work(self):
        while True:
            url = self.queue.get()
            Spider.crawl_page(threading.current_thread().name, url)
            self.queue.task_done()

    # Each queued link is a new job
    def create_jobs(self):
        for link in Spider.queue:
            self.queue.put(link)
        self.queue.join()
        if len(Spider.crawled) < StartPoint.MAX_CRAWL:
            self.crawl()

    # Check if there are items in the queue, if so crawl them
    def crawl(self):
        if len(Spider.queue) > 0 and len(Spider.crawled) < 10:
            print(str(len(Spider.queue)) + ' links in the queue')
            self.create_jobs()
            print(Spider.crawled)
            StartPoint.result.update(Spider.crawled)
            Spider.crawled.clear()
            Spider.queue.clear()

    def ret_val(self):
        return StartPoint.result

    def start(self):
        self.create_workers()
        self.crawl()
