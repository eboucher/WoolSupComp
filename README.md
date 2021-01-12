# WoolSupComp

Wool Supplier Comparator. This is a simple web-scraping program using Scrapy that retrieves certain some data such as price, needle size and wool composition of wool ball providers. It includes a spider that scrapes a single website, however it is intended to include other distributors later on.

## Technologies and requirements

I used python 3.8.5 along with pip for this project, so ideally you need to use at least a python version >=3.

I highly recommend to create a python virtual environment to work on this. You can create it by executing:

> virtualenv virtual_env

Once you activate it, you need to install Scrapy. You can do this with the following command:

> pip install scrapy

And finally, download the Pandas library to for data analysis and manipulation:

> pip install pandas

Now, you're all set. To execute a spider, run the command:

> scrapy crawl [spider_name]

In this project, there is only one spider for the Wollplatz website. So you run it by executing:

> scrapy crawl wollplatz_wool_balls

(1) Activate the virtual environment:

> source [env_name]/bin/activate


(2) In the /api directory, run 

> export FLASK_APP=server.py

to tell the terminal the application to work with by exporting the FLASK_APP environment variable. Then, execute:

> python -m flask run

To serve te declarated server in a production environment. It should display: Running on http://127.0.0.1:5000/


(3) Once the server is up and running, launch the web application by running:

> ng serve

in another terminal tab in the directory /webpage. It should display the following:

** Angular Live Development Server is listening on localhost:4200, open your browser on http://localhost:4200/ **