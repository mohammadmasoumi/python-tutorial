# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IrnaRSSItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    title = scrapy.Field()
    link = scrapy.Field()
    description = scrapy.Field()
    language = scrapy.Field()
    copyright = scrapy.Field()
    lastBuildDate = scrapy.Field()
    generator = scrapy.Field()
