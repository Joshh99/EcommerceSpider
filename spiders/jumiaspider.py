import scrapy


class JumiaspiderSpider(scrapy.Spider):
    name = "jumiaspider"
    allowed_domains = ["www.jumia.com.ng"]
    start_urls = ["https://www.jumia.com.ng/"]

    def parse(self, response):

        #main section division (24 sections - 12 product deals and 12 collection deals and 1 top selling items section)
        sections = response.css('div.col16.-pvs')

        # 12 product deals sections (11 + 1 flash sales)
        secdiv = sections.css('div.crs-w._main.-phxs')
        secdivdivs = secdiv.css('div.crs.row._no-g.-fw-nw._6cl-4cm.-pvxs')

        # select each product deal section
        secdivdiv1 = secdivdivs[0].css('div.itm.col article.prd._box._hvr')
        
        # printing details of products in second product deal section
        for product in secdivdiv1:
            yield {
            'price': product.css('a div.prc ::text').get(),
            'discount': product.css('a div.bdg._dsct ::text').get(),
            'name': product.css('a div.name::text').get()
        }

        # 11 collection deals sections (only scraping 'deals you can't miss section')
        cols = sections.css('div.row._no-g.-tac.-pvxs.-phs._6c-shs')

        # 11 collection deals sections hrefs 
        for col in cols: 
            yield{
                'link': col.css('a ::attr(href)').extract()
            }

        # top selling items
        top = response.css('div.col16.-mvs article.prd._box._hvr')

        # returns list of top selling items
        yield {
            'name_top': top.css('a div.name ::text').extract(),
            'price_top': top.css('a div.prc ::text').extract(),
            'discount_top': top.css('a div.bdg._dsct ::text').extract() 
        }
        

        
        # prod_rel_urls = response.css('div.-paxs.row._no-g._4cl-3cm-shs a::attr(href)').extract()
        
        # Request each individual page and parse response to parse_product_page function

    #     for prod_rel_url in prod_rel_urls:
    #         prod_url = 'https://www.jumia.com.ng' + prod_rel_url
    #         print(prod_url)
    #         yield scrapy.Request(prod_url, callback=self.parse_prod_page)

    # def parse_prod_page(self, response):
    #     price = response.css('div.df.-i-ctr.-fw-w.-pas.-brbl-fsale.-rad4-bot > span::text').get()

    #     yield {
    #         'url': response.url,
    #         'price': price
    #     }
        



# class JumiaspiderSpider(scrapy.Spider):
#     name = "jumiaspider"
#     allowed_domains = ["www.jumia.com.ng"]
#     start_urls = ["https://www.jumia.com.ng/"]

#     def parse(self, response):
#         flash_rel_url = response.css('.-pvs h2::text').get()

#         flash_page_url = 'https://www.jumia.com.ng/' + flash_rel_url

#         # Sends request for flash sales page and sends response to parse_flash_page function 
#         yield scrapy.Request(flash_page_url, callback=self.parse_flash_page)

#     def parse_flash_page(self, response):
#         """ Receives response for flash sale page. ALL flash sales parsing happens here."""

#         # A list of all the relative urls of each product
#         prod_rel_urls = response.css('div.-paxs.row._no-g._4cl-3cm-shs a::attr(href)').extract()
        
#         # Request each individual page and parse response to parse_product_page function
#         yield ['https://www.jumia.com.ng' + prod_rel_url for prod_rel_url in prod_rel_urls]
#         # for prod_rel_url in prod_rel_urls:
#         #     prod_url = 'https://www.jumia.com.ng' + prod_rel_url 
#     #         yield scrapy.Request(prod_url, callback=self.parse_product_page)

#     #     next_page = 


#     # def parse_product_page(self, response):
