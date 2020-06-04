import scrapy


class SportsSportingBetSpider(scrapy.Spider):
    name = 'SportsSporingBet'
    allowed_domains = []    


    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def start_requests(self):
        pass

    def parse(self, response):
        pass

