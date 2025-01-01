import scrapy

from scrapy import Request
from scrapy.selector import Selector
from miniature.items import ZackGameInformation


class ZackSpider(scrapy.Spider):
 
    name = 'zack'
    home = 'http://zackgame4.com'
    url = 'http://zackgame4.com/products/'
    
    custom_settings = {
        'CONCURRENT_REQUESTS': 10,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 10,
        'DOWNLOAD_DELAY': 5,
        'COOKIES_ENABLED': False,
        'HTTPCACHE_ENABLED': False,
        'FEED_FORMAT': 'json',
        'TOR_PROXY_ENABLED': True
    }

    def __init__(self, *args, **kwargs):
        super(ZackSpider, self).__init__(*args, **kwargs)
        

    def start_requests(self):
        yield Request(self.url, callback=self.process_page, dont_filter=True)

    def process_page(self, response):

        next_page = response.css('li.page_last a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.process_page)

        """Parse the product listing page."""
        products = response.xpath("//dl[@class='pro_item fir']").getall()

        for product_html in products:

            product = Selector(text=product_html)
            item = ZackGameInformation()
            item['name'] = product.xpath(".//div[@class='pro_name']/a/text()").get()
            item['price'] = float(product.xpath(".//span[@class='price_data PriceColor']/text()").get())
            relative_url = product.xpath(".//div[@class='pro_name']/a/@href").get()
            item['url'] = response.urljoin(relative_url)
   
            yield item

