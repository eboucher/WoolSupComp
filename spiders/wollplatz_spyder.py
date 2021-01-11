import scrapy
import pandas as pd
import openpyxl
import os

from constants.wollplatz import *

wool_balls = {
    'dmc':'natura-xl', 
    'drops':'safran', 
    'drops':'baby-merino-mix', 
    'hahn':'alpacca-speciale', 
    'stylecraft':'special-double-knit'
}


class WollplatzSpyder(scrapy.Spider):
    name = 'wollplatz_wool_balls'

    # Create dataframe first with columns only
    result_df = pd.DataFrame(columns=['Marke', 'Bezeichnung', 'Preis', 'Lieferzeit', 'Nadelstärke', 'Zusammenstellung'])

    def start_requests(self):
        urls = []

        # Get input data from excel file
        print("Getting data from file:\n" + os.getcwd() + INPUT_FILE + "\n")
        input_df = pd.read_excel(os.getcwd() + INPUT_FILE)
        print(input_df)
        
        for row in input_df.itertuples(index=False):
            Marke = row.Marke.replace(' ', '-').lower()
            Bezeichnung = row.Bezeichnung.replace(' ', '-').lower()
            print("Marke: ", Marke, "Bezeichnung: ", Bezeichnung)
            url = WOLLPLATZ_BASE_URL + 'wolle/' + Marke + '/' + Marke + '-' + Bezeichnung
            urls.append(url)
            yield scrapy.Request(url=url, meta={'Marke': Marke, 'Bezeichnung': Bezeichnung}, callback=self.parse)


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
        self.result_df = self.result_df.append(df1, ignore_index = True)

        # Export dataframe of items to CSV file
        filename = 'result_df.csv'
        self.result_df.to_csv(filename)

        yield {
            'Product price amount': price,
            'Product price currency': currency,
            'Needle size': needle_size,
            'Composition': wool_composition,
        }