import scrapy

from scrapy import Request
from scrapy.selector import Selector
from miniature.items import WartableInformation


class WartableSpider(scrapy.Spider):
 
    name = 'wartable'
    home = 'https://www.wartablegames.me'
    url = 'https://www.wartablegames.me/All-Products-c81336.html'
    
    custom_settings = {
        'CONCURRENT_REQUESTS': 10,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 10,
        'DOWNLOAD_DELAY': 5,
        'COOKIES_ENABLED': False,
        'HTTPCACHE_ENABLED': False,
        'FEED_FORMAT': 'json',
        'TOR_PROXY_ENABLED': False
    }

    def __init__(self, *args, **kwargs):
        super(WartableSpider, self).__init__(*args, **kwargs)
        

    def start_requests(self):
        yield Request(self.url, callback=self.process_page, dont_filter=True)

    def process_page(self, response):

        next_page = response.xpath("//a[@class='next']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.process_page)

        products = response.xpath("//div[@class='product_item']").getall()
    
        for product_html in products:

            product = Selector(text=product_html)
            item = WartableInformation()
            item['name'] = product.xpath(".//a[@class='name']/text()").get()
            price_text = product.xpath(".//div[@class='price']/text()").get()
            if price_text:
                item['price'] = float(price_text.replace('US$', ''))
            relative_url = product.xpath(".//a[@class='name']/@href").get()
            item['url'] = response.urljoin(relative_url)
   
            yield item

