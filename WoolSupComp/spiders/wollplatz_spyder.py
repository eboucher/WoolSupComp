import scrapy
import pandas as pd
import openpyxl

Wollplatz_base_url = "https://www.wollplatz.de/"

wool_balls = {
    'dmc':'natura-xl', 
    'drops':'saffron', 
    'drops':'baby-merino-mix', 
    'rooster':'alpacca-speciale', 
    'stylecraft':'special-double-knit'
}

# Selector for class="product-price-currency":
product_price_currency_selector = '//div[contains(@class, "shopholder")]//*[@id="ContentPlaceHolder1_pnlPDetailBuyHolder"]//div[contains(@class, "buy-price")]//span[@class="product-price"]//span[@class="product-price-currency"]//text()'
# Selector for class="product-price-amount":
product_price_amount_selector = '//div[contains(@class, "shopholder")]//*[@id="ContentPlaceHolder1_pnlPDetailBuyHolder"]//div[contains(@class, "buy-price")]//span[@class="product-price"]//span[@class="product-price-amount"]//text()'
# Selector for needle size:
needle_size_selector = '//div[contains(@class, "shopholder")]//*[@id="ContentPlaceHolder1_pnShortSpecs"]//div[contains(@class, "innerspecsholder")]//*[@id="pdetailTableSpecs"]//table//tr[td//text()[contains(., "Nadelstärke")]]//td[2]//text()'
# Selector for Composition:
wool_composition_selector = '//div[contains(@class, "shopholder")]//*[@id="ContentPlaceHolder1_pnShortSpecs"]//div[contains(@class, "innerspecsholder")]//*[@id="pdetailTableSpecs"]//table//tr[td//text()[contains(., "Zusammenstellung")]]//td[2]//text()'


class WollplatzSpyder(scrapy.Spider):
    name = 'wollplatz_wool_balls'

    dataframe = pd.DataFrame(columns=['Marke', 'Bezeichnung', 'Preis', 'Lieferzeit', 'Nadelstärke', 'Zusammenstellung'])

    def start_requests(self):
        urls = []

        for key, value in wool_balls.items():
            url = Wollplatz_base_url + 'wolle/' + key + '/' + key + '-' + value
            urls.append(url)

            # df2 = {'Marke': key, 'Bezeichnung': value, 'Preis': None, 'Lieferzeit': None, 'Nadelstärke': None, 'Zusammenstellung': None}
            # self.dataframe = self.dataframe.append(df2, ignore_index = True)

            yield scrapy.Request(url=url, meta={'Marke': key, 'Bezeichnung': value}, callback=self.parse)


    def parse(self, response):
        # import ipdb;ipdb.set_trace()
        page = response.url.split("/")[-2]
        print("\n" + "PAGE = " + str(page) + "\n")
        print("\n" + "META = " + str(response.meta) + "\n")

        brand = response.meta['Marke']
        model = response.meta['Bezeichnung']
        delivery = None
        price = response.xpath(product_price_amount_selector).get() + ' ' + response.xpath(product_price_currency_selector).get()
        # price = None
        needle_size = response.xpath(needle_size_selector).get()
        wool_composition = response.xpath(wool_composition_selector).get()


        df1 = {'Marke': brand, 'Bezeichnung': model, 'Preis': price, 'Lieferzeit': delivery, 'Nadelstärke': needle_size, 'Zusammenstellung': wool_composition}
        self.dataframe = self.dataframe.append(df1, ignore_index = True)
        
        print(self.dataframe)

        filename = 'dataframe.csv'
        self.dataframe.to_csv(filename)

        # import ipdb;ipdb.set_trace()

        # filename = f'wollplatz-{page}.html'
        # with open(filename, 'wb') as f:
            # result = response.xpath(product_price_currency).get()
            # f.write(result.encode('utf-8'))
            # result = response.xpath(product_price_amount).get()
            # f.write(result.encode('utf-8'))
            # result = response.xpath(needle_size).get()
            # f.write(result.encode('utf-8'))
            # result = response.xpath(wool_composition).get()
            # f.write(result.encode('utf-8'))
            # f.write(dataframe)
        # self.log(f'Saved file {filename}')

        yield {
            'Product price currency': response.xpath(product_price_currency_selector).get(),
            'Product price amount': response.xpath(product_price_amount_selector).get(),
            'Needle size': response.xpath(needle_size_selector).get(),
            'Composition': response.xpath(wool_composition_selector).get(),
        }


# Selector for delivery time
# (information not found in website, except for "Between 3 to 5 work days" by default for all products)




        # dataframe = pd.DataFrame()
        # dataframe.append(pd.DataFrame({'Preis': response.xpath(product_price_amount).get().encode('utf-8') + ' ' 
        #                                 + response.xpath(product_price_currency).get().encode('utf-8')}))
        # dataframe.append(pd.DataFrame('Lieferzeit', response.xpath(needle_size).get().encode('utf-8')
        # dataframe.append(pd.DataFrame({'Nadelstärke': response.xpath(needle_size).get().encode('utf-8')})
        # dataframe.append(pd.DataFrame({'Zusammenstellung': response.xpath(wool_composition).get().encode('utf-8')})

        # page = response.url.split("/")[-1]
        # filename = f'wollplatz-{page}.csv'