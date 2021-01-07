import scrapy

Wollplatz_base_url = "https://www.wollplatz.de/"

wool_balls = {
    'dmc':'natura-xl', 
    'drops':'saffron', 
    'drops':'baby-merino-mix', 
    'rooster':'alpacca-speciale', 
    'stylecraft':'special-double-knit'
}

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
            f.write(response.body)
        self.log(f'Saved file {filename}')
        for wool_ball in response.xpath('//span/text()'):
            yield {
                'Product price currency': wool_ball.xpath('//div[contains(@class, "shopholder")]//*[@id="ContentPlaceHolder1_pnlPDetailBuyHolder"]//div[contains(@class, "buy-price")]//span[@class="product-price"]//span[@class="product-price-currency"]').get(),
                'Product price amount': wool_ball.xpath('//div[contains(@class, "shopholder")]//*[@id="ContentPlaceHolder1_pnlPDetailBuyHolder"]//div[contains(@class, "buy-price")]//span[@class="product-price"]//span[@class="product-price-amount"]').get(),
                'Needle size': wool_ball.xpath('//div[contains(@class, "shopholder")]//*[@id="ContentPlaceHolder1_pnShortSpecs"]//div[contains(@class, "innerspecsholder")]//*[@id="pdetailTableSpecs"]//table//tbody//tr[td//text()[contains(., "Nadelstärke")]]').get(),
                'Composition': wool_ball.xpath('//div[contains(@class, "shopholder")]//*[@id="ContentPlaceHolder1_pnShortSpecs"]//div[contains(@class, "innerspecsholder")]//*[@id="pdetailTableSpecs"]//table//tbody//tr[td//text()[contains(., "Zusammenstellung")]]').get(),
            }



# Selector for class="product-price-currency":
# //div[contains(@class, "shopholder")]//*[@id="ContentPlaceHolder1_pnlPDetailBuyHolder"]//div[contains(@class, "buy-price")]//span[@class="product-price"]//span[@class="product-price-currency"]

# Selector for class="product-price-amount":
# //div[contains(@class, "shopholder")]//*[@id="ContentPlaceHolder1_pnlPDetailBuyHolder"]//div[contains(@class, "buy-price")]//span[@class="product-price"]//span[@class="product-price-amount"]


# Selector for needle size
# //div[contains(@class, "shopholder")]//*[@id="ContentPlaceHolder1_pnShortSpecs"]//div[contains(@class, "innerspecsholder")]//*[@id="pdetailTableSpecs"]//table//tbody//tr[td//text()[contains(., "Nadelstärke")]]

# Selector for Composition
# //div[contains(@class, "shopholder")]//*[@id="ContentPlaceHolder1_pnShortSpecs"]//div[contains(@class, "innerspecsholder")]//*[@id="pdetailTableSpecs"]//table//tbody//tr[td//text()[contains(., "Zusammenstellung")]]

# Selector for delivery time
# (information not found in website, except for "Between 3 to 5 work days" by default for all products)