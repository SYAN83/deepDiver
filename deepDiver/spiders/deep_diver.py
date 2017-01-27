from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider


class DeepSpider(CrawlSpider):

    name = 'physics'
    allowed_domains = ['physics.sc.edu']
    start_urls = ['http://www.physics.sc.edu']
    count = 10
    rules = (
        Rule(LinkExtractor(allow=(), deny=('robots\.txt',)), callback="parse_items", follow=True),
    )

    # def __init__(self, start_urls, n=-1):
    #
    # def start_requests(self):
    #     for url in self.start

    def parse_items(self, response):
        if response.status / 10 == 20:
            self.logger.info(msg='\n\tON SUCCESS: {0}'.format(response.url,))
        if response.status / 10 == 40:
            self.logger.error(msg='\n\tCLIENT ERROR: {0}'.format(response.url, ))
        # print response.url
        self.count -= 1
        if self.count == 0:
            raise CloseSpider('bandwidth_exceeded')