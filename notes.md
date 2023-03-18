-
- https://www.whiskyshop.com/blended-scotch-whisky?item_availability=In+Stock
- https://scrapeops.io/python-scrapy-playbook/scrapy-403-unhandled-forbidden-error/
- https://towardsdatascience.com/scrapy-this-is-how-to-successfully-login-with-ease-ea980e2c5901
- https://stackoverflow.com/questions/5850755/using-scrapy-with-authenticated-logged-in-user-session
- https://www.youtube.com/watch?v=s4jtkzHhLzY
- http://quotes.toscrape.com/login
- https://www.kite.com/blog/python/web-scraping-scrapy/

```
>>> url = 'https://www.whiskyshop.com/blended-scotch-whisky'
>>> fetch(url)
>>> response.status
>>> products = response.css('div.product-item-info')
>>> products.css('a.product-item-link').get()
>>> products.css('a.product-item-link::text').get()
>>> products.css('span.price::text').get().replace('£', '')
>>> products.css('a.product-item-link').attrib['href']
```
