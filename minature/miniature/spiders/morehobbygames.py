import scrapy

from scrapy import Request
from scrapy.selector import Selector
from miniature.items import MorehobbygamesInformation

class MorehobbygamesSpider(scrapy.Spider):
 
    name = 'morehobbygames'
    home = 'https://www.morehobbygames.com'
    url = 'https://www.morehobbygames.com/10-warhammer-40000-'
    
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
        super(MorehobbygamesSpider, self).__init__(*args, **kwargs)
        

    def start_requests(self):
        yield Request(self.url, callback=self.process_page, dont_filter=True)

    def process_page(self, response):

        next_page = response.xpath("//a[@aria-label='Next']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.process_page)

        products = response.xpath("//div[@class='thumbnail-container']").getall()
    
        for product_html in products:

            product = Selector(text=product_html)
            item = MorehobbygamesInformation()
            item['name'] = product.xpath(".//h2[@itemprop='name']/a/text()").get()
            price_text = product.xpath(".//span[@itemprop='price']/text()").get()
            regular_price_text = product.xpath(".//span[@class='regular-price']/text()").get()
            if price_text:
                item['price'] = self.parse_price(price_text)
            if regular_price_text:
                item['regular_price'] = self.parse_price(regular_price_text)
            relative_url = product.xpath(".//div[@class='product-thumbnail-wrapper relative']/a/@href").get()
            item['url'] = response.urljoin(relative_url)
   
            yield item

    def parse_price(self, price_text):
        return float(price_text.replace(' €', '').replace("\n", "").replace(" ", "").replace("\xa0€", "").replace(",","."))

