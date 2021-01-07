import scrapy
import pandas as pd
import openpyxl

from WoolSupComp.selectors.wollplatz import *

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

    # Create dataframe first with columns only
    dataframe = pd.DataFrame(columns=['Marke', 'Bezeichnung', 'Preis', 'Lieferzeit', 'Nadelstärke', 'Zusammenstellung'])

    def start_requests(self):
        urls = []

        # Iterate through pages corresponding to each item
        for key, value in wool_balls.items():
            url = Wollplatz_base_url + 'wolle/' + key + '/' + key + '-' + value
            urls.append(url)
            yield scrapy.Request(url=url, meta={'Marke': key, 'Bezeichnung': value}, callback=self.parse)


    def parse(self, response):

        # Brand and model retrieved from parameters
        brand = response.meta['Marke']
        model = response.meta['Bezeichnung']

        # Delivery time non-existing for this provider
        delivery = None

        # Price, needle size and wool composition are retrieved from the website's HTML
        price = response.xpath(PRODUCT_PRICE_AMOUNT_SELECTOR).get()
        currency = response.xpath(PRODUCT_PRICE_CURRENCY_SELECTOR).get()
        needle_size = response.xpath(NEEDLE_SIZE_SELECTOR).get()
        wool_composition = response.xpath(WOOL_COMPOSITION_SELECTOR).get()

        # Create dataframe for current parsed item
        df1 = {
            'Marke': brand, 
            'Bezeichnung': model, 
            'Preis': price + ' ' + currency, 
            'Lieferzeit': delivery, 
            'Nadelstärke': needle_size, 
            'Zusammenstellung': wool_composition
        }
        
        # Add current item value to global dataframe of items
        self.dataframe = self.dataframe.append(df1, ignore_index = True)

        # Export dataframe of items to CSV file
        filename = 'dataframe.csv'
        self.dataframe.to_csv(filename)

        yield {
            'Product price amount': price,
            'Product price currency': currency,
            'Needle size': needle_size,
            'Composition': wool_composition,
        }