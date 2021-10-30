import scrapy


class DicaSpider(scrapy.Spider):


    name = 'dica'
    #allowed_domains = ['boadica.com.br']
    #start_urls = ['https://www.boadica.com.br/pesquisa/mem_cpu/precos?ClasseProdutoX=3&CodCategoriaX=14&XT=8&XG=5']
    start_urls = ['https://www.kabum.com.br/hardware/memoria-ram/ddr-3?page_number=8&page_size=20&facet_filters=&sort=most_searched']

    def parse(self, response):
        for tudo in response.css('.iHoWna'):

            yield {
                'titulo': tudo.css('.nameCard::text').get(),

                'preco':tudo.css('.priceCard::text').get()

            }
        pass
