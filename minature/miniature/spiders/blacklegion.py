import scrapy

from scrapy import Request
from scrapy.selector import Selector
from miniature.items import BlacklegionInformation


class BlacklegionSpider(scrapy.Spider):
 
    name = 'blacklegion'
    home = 'https://blacklegionmarket.co'
    url = 'https://blacklegionmarket.co/product-category/warhammer'
    
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
        super(BlacklegionSpider, self).__init__(*args, **kwargs)
        

    def start_requests(self):
        yield Request(self.url, callback=self.process_page, dont_filter=True)

    def process_page(self, response):

        next_page = response.xpath("//a[@class='next page-numbers']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.process_page)

        products = response.xpath("//div[contains(@class, 'content-product')]").getall()
    

        for product_html in products:

            product = Selector(text=product_html)
            item = BlacklegionInformation()
            item['name'] = product.xpath(".//h2[@class='product-title']/a/text()").get()
            price_text = product.xpath(".//span[@class='woocommerce-Price-amount amount']/bdi/text()").get()
            print(price_text)
            if price_text:
                item['price'] = float(price_text.replace('$', ''))
            relative_url = product.xpath(".//h2[@class='product-title']/a/@href").get()
            item['url'] = response.urljoin(relative_url)
   
            yield item

