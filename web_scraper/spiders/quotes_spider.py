import scrapy


def convertToString(encodedString):
    return encodedString.encode("utf-8").decode("unicode_escape").encode("ascii", "ignore")


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        url = "http://quotes.toscrape.com/"
        tag = getattr(self, "tag", None)
        if tag is not None:
            url = url + "tag/" + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for quote in response.css("div.quote"):
            string_text = convertToString(quote.css("span.text::text").extract_first()).decode("utf-8")
            yield {
                "text": string_text,
                "author": quote.css("small.author::text").get(),
            }

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
