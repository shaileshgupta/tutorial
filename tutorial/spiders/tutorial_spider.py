import scrapy
from tutorial.items import TutorialItem

class TutorialSpider(scrapy.Spider):
	name = "tutorial"
	allowed_domains = ["dmoz.org"]
	start_urls = [
		"http://www.dmoz.org/Computers/Programming/Languages/Python/"
	]

	def parse(self, response):
		
		for sel in response.xpath("//div[@class='title-and-desc']"):
			item = TutorialItem()
			item['title'] = sel.xpath('a/div/text()').extract()
			item['link'] = sel.xpath('a/@href').extract()
			item['desc'] = sel.xpath('div/text()').extract()
			yield item