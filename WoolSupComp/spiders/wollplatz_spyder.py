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
currency = '//div[contains(@class, "shopholder")]//*[@id="ContentPlaceHolder1_pnlPDetailBuyHolder"]//div[contains(@class, "buy-price")]//span[@class="product-price"]//span[@class="product-price-currency"]//text()'

# Selector for class="product-price-amount":
amount = '//div[contains(@class, "shopholder")]//*[@id="ContentPlaceHolder1_pnlPDetailBuyHolder"]//div[contains(@class, "buy-price")]//span[@class="product-price"]//span[@class="product-price-amount"]//text()'

# Selector for needle size:
needle = '//div[contains(@class, "shopholder")]//*[@id="ContentPlaceHolder1_pnShortSpecs"]//div[contains(@class, "innerspecsholder")]//*[@id="pdetailTableSpecs"]//table//tr[td//text()[contains(., "Nadelstärke")]]'

# Selector for Composition:
composition = '//div[contains(@class, "shopholder")]//*[@id="ContentPlaceHolder1_pnShortSpecs"]//div[contains(@class, "innerspecsholder")]//*[@id="pdetailTableSpecs"]//table//tr[td//text()[contains(., "Zusammenstellung")]]'


class WollplatzSpyder(scrapy.Spider):
    name = 'wollplatz_wool_balls'

    def start_requests(self):
        urls = []

        for key, value in wool_balls.items():
            print(Wollplatz_base_url + 'wolle/' + key + '/' + key + '-' + value)
            urls.append(Wollplatz_base_url + 'wolle/' + key + '/' + key + '-' + value)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        page = response.url.split("/")[-1]
        print("\n" + "PAGE = " + str(page) + "\n")
        filename = f'wollplatz-{page}.html'
        with open(filename, 'wb') as f:
            # f.write(response.body)
            result = response.xpath(currency).get()
            f.write(result.encode('utf-8'))
            result = response.xpath(amount).get()
            f.write(result.encode('utf-8'))
            result = response.xpath(needle).get()
            f.write(result.encode('utf-8'))
            result = response.xpath(composition).get()
            f.write(result.encode('utf-8'))
        self.log(f'Saved file {filename}')

        print('\nProduct price currency = ' + response.xpath(currency).get())
        print("\n")
        print('\nProduct price amount = ' + response.xpath(amount).get())
        print("\n")
        print('\nNeedle size = ' + response.xpath(needle).get())
        print("\n")
        print('\nComposition = ' + response.xpath(composition).get())
        print("\n")

        yield {
            'Product price currency': response.xpath(currency).get(),
            'Product price amount': response.xpath().get(),
            'Needle size': response.xpath(needle).get(),
            'Composition': response.xpath(composition).get(),
        }


# Selector for delivery time
# (information not found in website, except for "Between 3 to 5 work days" by default for all products)