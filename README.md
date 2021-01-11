# WoolSupComp

Wool Supplier Comparator. This is a simple web-scraping program using Scrapy that retrieves certain some data such as price, needle size and wool composition of wool ball providers. It includes a spider that scrapes a single website, however it is intended to include other distributors later on.

## Technologies and requirements

I used python 3.8.5 along with pip for this project, so ideally you need to use at least a python version >=3.

I highly recommend to create a python virtual environment to work on this. You can create it by executing:

> virtualenv virtual_env

Once you activate it, you need to install Scrapy. You can do this with the following command:

> pip install scrapy

I also use the pandas library by using the command:

> pip install pandas

And finally, a Python library to read/write Excel xlsx/xlsm files, openpyxl:

> pip install openpyxl

Well, also xlrd...

> pip install xlrd

Now, you're all set. To execute a spider, run the command:

> scrapy crawl [spider_name]

In this project, there is only one spider for the Wollplatz website. So you run it by executing:

> scrapy crawl wollplatz_wool_balls

