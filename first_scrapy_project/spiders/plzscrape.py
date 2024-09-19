import scrapy


class PlzscrapeSpider(scrapy.Spider):
    # The name of the spider
    name = "plzscrape"
    # The domains that are allowed (links to other domains are skipped)
    allowed_domains = ["plzscrape.com"]
    # The URLs to start with
    start_urls = ["https://plzscrape.com/basic/html-elements"]

    def parse(self, response):
        # Extract the h1 heading
        h1_heading = response.css('h1::text').get()
        
        # extract all sections
        sections = response.css('section')
        
        for section in sections:
            h2_heading = section.css('h2::text').get()
            paragraphs = section.css('p::text').getall()
            
            # Yield a dictionary with the data
            yield {
                'h1': h1_heading,
                'h2': h2_heading,
                'paragraphs': paragraphs
            }
