import scrapy
from scrapy.http import FormRequest, Request

class WhiskySpider(scrapy.Spider):
    name = "whisky"
    # start_urls = ['https://www.whiskyshop.com/blended-scotch-whisky']

    def start_requests(self):
        url = 'https://www.whiskyshop.com/customer/account/login/referer/aHR0cHM6Ly93d3cud2hpc2t5c2hvcC5jb20vY29udGFjdA%2C%2C/'
        yield scrapy.Request(url, callback=self.login)

    def login(self, response):
        # token = response.css('form input[name=form_key]::attr(value)').extract_first()
        data = {'login[username]': 'jamesdavis@lsu.edu', 'login[password]': 'SQLSaturday'}
        yield FormRequest.from_response(response, formid='login-form',
            formdata=data, callback=self.after_login)

    def after_login(self, response):
        url = 'https://www.whiskyshop.com/blended-scotch-whisky'
        return Request(url=url, callback=self.parse_whisky)

    def parse_whisky(self, response):
        for product in response.css('div.product-item-info'):
            try:
                yield {
                    'name': product.css('a.product-item-link::text').get(),
                    'price': product.css('span.price::text').get().replace('£', ''),
                    'link': product.css('a.product-item-link').attrib['href']
                }
            except:
                yield {
                    'name': product.css('a.product-item-link::text').get(),
                    'price': 'out of stock',
                    'link': product.css('a.product-item-link').attrib['href']
                }

        next_page = response.css('a.action.next').attrib['href']

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse_whisky)
