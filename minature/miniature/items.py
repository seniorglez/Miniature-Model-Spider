# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class ZackGameInformation(Item):
    url = Field(type=str)
    name = Field(type=str)
   
    #price
    price = Field(type=float)

class BlacklegionInformation(Item):
    url = Field(type=str)
    name = Field(type=str)
   
    #price
    price = Field(type=float)

class WartableInformation(Item):
    url = Field(type=str)
    name = Field(type=str)
   
    #price
    price = Field(type=float)

class MorehobbygamesInformation(Item):
    url = Field(type=str)
    name = Field(type=str)
   
    #price
    regular_price = Field(type=float)
    price = Field(type=float)
  