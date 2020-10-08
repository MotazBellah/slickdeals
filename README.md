# Computer Deals

Build a Crawler which will crawl all the computer from all the available pages
the goal is to visit each page and scrape the "title", the "price" and the "store" from all the available pages.
- https://slickdeals.net/computer-deals/

## Code style

- This project is written in python 3.
- Use selenium.

## Clone/Run app
````
# Clone repo
$ git clone https://github.com/MotazBellah/slickdeals

# Install all dependencies
$ pip install -r requirements.txt

# Run
$ cd silkdeals
$ scrapy crawl computerdeals -o computers.csv

````
