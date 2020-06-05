import scrapy


class SportsSportingBetSpider(scrapy.Spider):
    name = 'SportsSportingBet'
    allowed_domains = ['https://sports.sportingbet.com/']

    start_urls = ['https://sports.sportingbet.com/en/sports/football-4']


    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    # def start_requests(self):
    #     pass

    def parse(self, response):
        xpath_base_element = "//ms-event[@class='grid-event " \
                                                "ms-active-highlight " \
                                                "ng-star-inserted']"
        for item in response.xpath(xpath_base_element).getall():
            item = scrapy.Selector(text=item)
            res = item.xpath('//a/div/ms-option-group/ms-option/ms-event-pick/div/div/ms-font-resizer/text()')
            print(res.get())

