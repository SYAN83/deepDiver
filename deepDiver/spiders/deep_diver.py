from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
import logging
from scrapy.utils.log import configure_logging
from deepDiver.items import EmailItem

class DeepSpider(CrawlSpider):

    name = 'get_email'
    allowed_domains = ['harvard.edu']
    start_urls = ['http://www.harvard.edu']
    count = 10
    rules = (
        Rule(LinkExtractor(allow=(), deny=('robots.txt',)), callback='parse_items', follow=True),
    )

    def __init__(self, *args, **kwargs):
        log_setting = {
            'LOG_FILE': 'crawl.log',
            'LOG_LEVEL': logging.DEBUG
        }
        configure_logging(settings=log_setting, )
        super(DeepSpider, self).__init__(*args, **kwargs)

    def parse_items(self, response):
        if response.status / 10 == 20:
            self.logger.info(msg=u'ON SUCCESS: {0}'.format(response.url,))

        if response.status / 10 == 40:
            self.logger.error(msg=u'CLIENT ERROR: {0}'.format(response.url, ))
        # print response.url
        self.count -= 1
        if self.count == 0:
            # self.logfile.close()
            raise CloseSpider('bandwidth_exceeded')

        mailto = response.xpath('//a[contains(@href, "mailto:")]/@href').extract()

        email_item = EmailItem()
        email_item['page_url'] = response.url
        email_item['email_cnt'] = len(mailto)

        return email_item