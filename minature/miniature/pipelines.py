# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class ZACKPipeline:

    def open_spider(self, spider):
        pass  # No action needed when the spider opens

    def process_item(self, item, spider):
        return item  # Return the item as-is, without any processing

    def close_spider(self, spider):
        pass  # No action needed when the spider closes