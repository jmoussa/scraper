import scrapy
from bs4 import BeautifulSoup


def convertToString(encodedString):
    return encodedString.encode("utf-8").decode("unicode_escape").encode("ascii", "ignore")


class YelpSpider(scrapy.Spider):
    name = "yelp"
    allowed_domains = ["yelp.com"]
    start_urls = ["https://www.yelp.com/search?find_desc=Restaurants&find_loc=Monmouth+Junction%2C+NJ+08852&ns=1"]

    def parse(self, response):
        names = response.css(".heading--h3__373c0__1n4Of").extract()
        reviews = response.css(".reviewCount__373c0__2r4xT::text").extract()

        # Give the extracted content row wise
        for item in zip(names, reviews):
            # create a dictionary to store the scraped info
            all_items = {
                "name": BeautifulSoup(item[0]).text,
                "reviews": item[1],
            }
            # yield or give the scraped info to scrapy
            yield all_items
