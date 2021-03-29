# Web Scraper

## Quotes Scraper

Scrape quotes from a quote generator

## Zillow Scraper

Scrape housing data from nearby and store in a dataframe and make available as an API with various tweaks and filters.

## Running the scraper

This project uses [scrapy](https://docs.scrapy.org/en/latest/index.html)

In order to run you will use the scrapy cli and enter the following. After it runs there should be a scraper.json file that is outputted containing the formatted information

```bash
scrapy crawl quotes
scrapy crawl zillow
```
