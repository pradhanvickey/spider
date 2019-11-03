import threading
import argparse
from queue import Queue
from spider import Spider
from domain import *
from general import *
from time import  time

def parse_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("--project_name",help="directory where queue and crawled file will be stored.",required=True)
    parser.add_argument("--page_url",help="url for which crawling need to be done.",required=True)
    parser.add_argument("--no_of_threads",help="no. of threads for crawling. Default is 1. ",default=1,type=int)
    args = parser.parse_args()
    return args

start_time = time()
options = parse_argument()
PROJECT_NAME = options.project_name
HOMEPAGE = options.page_url
DOMAIN_NAME = get_domain_name(HOMEPAGE)
NUMBER_OF_THREADS = options.no_of_threads
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

# Create worker threads (will die when main exits)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# Do the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


# Each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


# Check if there are items in the queue, if so crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()

create_workers()
crawl()
end_time = time()

print('Total time => ',str((end_time-start_time)*1000) +"ms")
