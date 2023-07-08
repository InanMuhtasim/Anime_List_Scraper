import scrapy


class AnimeItem(scrapy.Item):
    Serial = scrapy.Field()
    Name = scrapy.Field()
    Full_Info = scrapy.Field()
