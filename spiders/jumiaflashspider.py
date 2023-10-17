import scrapy
from Ecommerce_scraper.items import EcommerceScraperItem

class JumiaflashspiderSpider(scrapy.Spider):
    name = "jumiaflashspider"
    allowed_domains = ["www.jumia.com.ng"]
    start_urls = ["https://www.jumia.com.ng/flash-sales/"]

    custom_settings = {
        'FEEDS': { 'products.csv': { 'format': 'csv', 'overwrite': True}
                   }
        }

    def parse(self, response):
        """ Returns the discount on the first page and moves to the next page until the last page."""
        # # Returns list of discounts on each page
        # disc_responses = response.css('div.bdg._dsct._sm')
        # for disc in disc_responses:
        #     yield {
        #         'disc': disc.css('::text').get()
        #     }

        # Generate each product url
        prod_rel_urls = response.css('article.prd._fb._p.col.c-prd a.core::attr(href)').extract()
        for prod_rel_url in prod_rel_urls:
                prod_url = 'https://www.jumia.com.ng' + prod_rel_url
                yield scrapy.Request(prod_url, callback=self.parse_prod_page)

        # NEXT PAGE url generation
        next_page_response = response.css('div.pg-w.-ptm.-pbxl a[aria-label*="Next Page"]::attr(href)').get()
        if next_page_response:
            next_url = 'https://www.jumia.com.ng' + next_page_response
            yield response.follow(next_url, callback=self.parse)

    def parse_prod_page(self, response):
        """ Gets the key info from each product's page. """

        ecommerce_item = EcommerceScraperItem()
                
        ecommerce_item['name'] = response.css('h1.-fs20.-pts.-pbxs::text').get()
        ecommerce_item['brand'] = response.css('div.-pvxs a:nth-child(1)::text').get()
        ecommerce_item['new_price'] = response.css('div.df.-i-ctr.-fw-w.-pas.-brbl-fsale.-rad4-bot span::text').get()
        ecommerce_item['old_price'] = response.css('span.-tal.-gy5.-lthr.-fs16.-pvxs::text').get()
        ecommerce_item['disc_perc'] = response.css('span.bdg._dsct._dyn.-mls::text').get()
        ecommerce_item['rating'] = response.css('div.stars._m._al::text').get()
        ecommerce_item['key_features'] = response.css('div.markup.-pam ul li').extract()
        ecommerce_item['specs'] = response.css('div.card-b.-fh ul li').extract()
        ecommerce_item['imgs'] = response.css('div.sldr._img._prod.-rad4.-oh.-mbs ::attr(href)')
        
        yield ecommerce_item
                

            
               
        

        