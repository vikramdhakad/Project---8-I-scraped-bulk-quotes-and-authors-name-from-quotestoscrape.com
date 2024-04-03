import scrapy


class ScrapersSpider(scrapy.Spider):
    name = "scrapers"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/page/1/"]

    def parse(self, response):
            
        for nxt in response.css("li>a"):
            page = nxt.css("::attr(href)").get()
            ab_url = response.urljoin(page)
            yield response.follow(url=ab_url,callback=self.parse)
            
            for alldata in response.css("div.quote"):
                title = alldata.css("span.text::text").get()
                write = alldata.css(".author::text").get()
                tags = alldata.css(".tag::text").getall()
                yield{
                    "Quotes": title,
                    "Author Name": write,
                    "Tags": tags
                }
            
            
            
       