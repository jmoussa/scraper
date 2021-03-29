import scrapy
from bs4 import BeautifulSoup


def convertToString(encodedString):
    return encodedString.encode("utf-8").decode("unicode_escape").encode("ascii", "ignore")


class ZillowSpider(scrapy.Spider):
    name = "zillow"
    allowed_domains = ["zillow.com"]
    # TODO: Implement JSON based config and store master url there
    start_urls = [
        "https://www.zillow.com/homes/for_rent/?userPosition=-73.9283,40.7706&userPositionBounds=40.775600000000004,-73.9233,40.7656,-73.93329999999999&currentLocationSearch=true&searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-74.03141330986355%2C%22east%22%3A-73.87176822929715%2C%22south%22%3A40.6942256300102%2C%22north%22%3A40.79605799542918%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22ac%22%3A%7B%22value%22%3Atrue%7D%2C%22lau%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%7D"
    ]

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
