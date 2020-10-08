# -*- coding: utf-8 -*-
import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.keys import Keys
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from shutil import which
import time



class ComputerdealsSpider(scrapy.Spider):
    name = 'computerdeals'
    allowed_domains = ['slickdeals.net']
    start_urls = ['https://slickdeals.net/computer-deals/']

    # def start_requests(self):
    #     yield SeleniumRequest(
    #         url="https://slickdeals.net/computer-deals/",
    #         wait_time=3,
    #         callback=self.parse
    #     )

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        chrome_path = which("chromedriverr")

        self.driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
        # self.driver = webdriver.Chrome()


    def parse(self, response):
        self.driver.get("https://slickdeals.net/computer-deals")
        time.sleep(5)
        while True:


            html = self.driver.page_source
            response_obj = Selector(text=html)
            products = response_obj.xpath("//ul[@class='dealTiles categoryGridDeals']/li")

            for product in products:
                yield {
                    "name": product.xpath(".//a[@class='itemTitle bp-c-link']/text()").get(),
                    "link": product.xpath(".//a[@class='itemTitle bp-c-link']/@href").get(),
                    "store_name": product.xpath(".//button[@class='itemStore bp-p-storeLink bp-c-linkableButton bp-c-button--link  bp-c-button']/text()").get(),
                    "price": product.xpath("normalize-space(.//div[@class='itemPrice  wide ']/text())").get(),
                    "URL": self.driver.current_url,
                }
                
            try:
                next = self.driver.find_element_by_xpath("//a[@data-role='next-page']")
                next.click()
            except:
                break

        self.driver.close()


            # next_page = response_obj.xpath("//a[@data-role='next-page']")
            # try:
            #     next_page.click()
            # except:
            #     break
        # if next_page:
        #     absolute_url = f"https://slickdeals.net{next_page}"
        #     yield SeleniumRequest(
        #         url=absolute_url,
        #         wait_time=3,
        #         callback=self.parse
        #     )
