import scrapy

Wollplatz_base_url = "https://www.wollplatz.de/"

wool_balls = {
    'dmc':'natura-xl', 
    'drops':'saffron', 
    'drops':'baby-merino-mix', 
    'rooster':'alpacca-speciale', 
    'stylecraft':'special-double-knit'
}

# Selector for class="product-price-currency":
product_price_currency = '//div[contains(@class, "shopholder")]//*[@id="ContentPlaceHolder1_pnlPDetailBuyHolder"]//div[contains(@class, "buy-price")]//span[@class="product-price"]//span[@class="product-price-currency"]//text()'

# Selector for class="product-price-amount":
product_price_amount = '//div[contains(@class, "shopholder")]//*[@id="ContentPlaceHolder1_pnlPDetailBuyHolder"]//div[contains(@class, "buy-price")]//span[@class="product-price"]//span[@class="product-price-amount"]//text()'

# Selector for needle size:
needle_size = '//div[contains(@class, "shopholder")]//*[@id="ContentPlaceHolder1_pnShortSpecs"]//div[contains(@class, "innerspecsholder")]//*[@id="pdetailTableSpecs"]//table//tr[td//text()[contains(., "Nadelstärke")]]//td[2]//text()'

# Selector for Composition:
wool_composition = '//div[contains(@class, "shopholder")]//*[@id="ContentPlaceHolder1_pnShortSpecs"]//div[contains(@class, "innerspecsholder")]//*[@id="pdetailTableSpecs"]//table//tr[td//text()[contains(., "Zusammenstellung")]]//td[2]//text()'


class WollplatzSpyder(scrapy.Spider):
    name = 'wollplatz_wool_balls'

    def start_requests(self):
        urls = []

        for key, value in wool_balls.items():
            urls.append(Wollplatz_base_url + 'wolle/' + key + '/' + key + '-' + value)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = f'wollplatz-{page}.html'
        with open(filename, 'wb') as f:
            result = response.xpath(product_price_currency).get()
            f.write(result.encode('utf-8'))
            result = response.xpath(product_price_amount).get()
            f.write(result.encode('utf-8'))
            result = response.xpath(needle_size).get()
            f.write(result.encode('utf-8'))
            result = response.xpath(wool_composition).get()
            f.write(result.encode('utf-8'))
        self.log(f'Saved file {filename}')

        yield {
            'Product price currency': response.xpath(product_price_currency).get(),
            'Product price amount': response.xpath(product_price_amount).get(),
            'Needle size': response.xpath(needle_size).get(),
            'Composition': response.xpath(wool_composition).get(),
        }


# Selector for delivery time
# (information not found in website, except for "Between 3 to 5 work days" by default for all products)