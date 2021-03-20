# Web Scraper

I'm building some kind of webscraper with python and scapy. Will hopefully be the start of a nice data pipeline.


## Yelp Scraper

Scrapes reviews from restaurants in the area.
Will modify later on to accept location as input.
Maybe create a restaurant picker application.

## Running the scraper

This project uses [scrapy](https://docs.scrapy.org/en/latest/index.html)

In order to run you will use the scrapy cli and enter the following. After it runs there should be a scraper.json file that is outputted containing the formatted information

```bash
scrapy crawl quotes
scrapy crawl yelp 
```
