import scrapy
from selenium import webdriver
from tutorial.items import TutorialItem

class TutorialSpider(scrapy.Spider):
	name = "tutorial"
	allowed_domains = ["craigslist.co.in"]
	start_urls = [
		"http://delhi.craigslist.co.in/search/jjj"
	]

	def parse(self, response):
		for href in response.xpath("//div[@class='rows']/p/span/span/a/@href"):
			url = response.urljoin(href.extract())
			yield scrapy.Request(url, callback=self.parse_post_content)

		next_page = response.xpath("//div[@class='paginator buttongroup  firstpage']//a[@class='button next']/@href")
		if next_page:
			next_url = response.urljoin(next_page[0].extract())
			yield scrapy.Request(next_url, callback=self.parse)

	def parse_post_content(self, response):
		item = TutorialItem()
		item['title'] = response.xpath("//span[@id='titletextonly']/text()").extract()
		item['link'] = response.url
		item['desc'] = response.xpath("//section[@id='postingbody']/text()").extract()
		yield item