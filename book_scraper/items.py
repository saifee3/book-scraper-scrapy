import scrapy

class BookScraperItem(scrapy.Item):
    category = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    availability = scrapy.Field()
    rating = scrapy.Field()
    image_url=scrapy.Field()