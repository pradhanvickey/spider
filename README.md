# Web Crawler

Web Crawler to crawl all internal webpages of an URL and dump data in elastic search.

Steps to run:

-------------

1.sudo /etc/init.d/elasticsearch start

2.download files from  https://github.com/pradhanvickey/spider.git to a directory

3.cd directory_name(where files are downloaded)

4.python ./wrapper_script.py --config_file spider_config.json &

Note:
Please make changes in spider_config.json to crawl multiple url.

Eternal libraries used:
-----------------------

1.beautifulsoup4

2.lxml

3.requests

4.elasticsearch

Tested on:
----------

Python version - 3.7

elasticsearch version - 7.4.1
