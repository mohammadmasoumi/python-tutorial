from scrapy.spiders import XMLFeedSpider

from ..items import IrnaRSSItem

class IrnaRssSpider(XMLFeedSpider):
    name = "irna_rss"
    allowed_domains = ["irna.ir"]
    start_urls = ["https://irna.ir/rss"]
    iterator = "iternodes"
    itertag = 'item'


    def parse_node(self, response, node):
        self.logger.info(
            "Hi, this is a <%s> node!: %s", self.itertag, "".join(node.getall())
        )

        item = IrnaRSSItem()

        item["title"] = node.xpath("title/text()").get()
        item["link"] = node.xpath("link/text()").get()
        item["description"] = node.xpath("description/text()").get()
        item["language"] = node.xpath("language/text()").get()
        item["copyright"] = node.xpath("copyright/text()").get()
        item["lastBuildDate"] = node.xpath("lastBuildDate/text()").get()
        item["generator"] = node.xpath("generator/text()").get()
        # "/html/body/section/main/div/div/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div[6]/div/div[2]/a/h2"
        return item
