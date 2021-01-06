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
        # for wool_ball in response.xpath("//div[@class='wool']"):
        #     yield {
        #         'Author': wool_ball.xpath('.//span/a/@href').get(),
        #     }