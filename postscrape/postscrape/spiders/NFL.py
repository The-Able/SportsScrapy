from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class NFL(CrawlSpider):
    name = "nfl.com"
    allowed_domains = ['nfl.com']
    start_urls = ['https://www.nfl.com/players/']


    #next_buttonDetails =  LinkExtractor(restrict_xpaths='//a[@class="nfl-o-table-pagination__next"]')
    '''  
    SpecificPlayerDetails = LinkExtractor(restrict_xpaths='//a[@class="d3-o-player-fullname nfl-o-cta--link"]')
    StasButtonDetails = LinkExtractor(restrict_xpaths='//*[@id="main-content"]/section[1]/div/div/ul/li[2]')
    nextButtonDetails = LinkExtractor(restrict_xpaths="//a[@title='Next']")
    '''
    '''
   
    ruleSpecificPlaye = Rule(SpecificPlayerDetails, follow=True)
    ruleStasButton = Rule(StasButtonDetails, callback='parse_item', follow=True)
    rulenextButton = Rule(nextButtonDetails, follow=True)
    '''
    AllPlayersLinkDetails = LinkExtractor(restrict_xpaths='//li[@class="d3-o-tabs__list-item "]')
    NextDetails = LinkExtractor(restrict_xpaths='//a[@class="nfl-o-table-pagination__next"]')
    specificPlayerDetails = LinkExtractor(restrict_xpaths='//a[@class="d3-o-player-fullname nfl-o-cta--link"]')

    ruleAllPlayersDetail = Rule(AllPlayersLinkDetails)
    ruleNextDetails = Rule(NextDetails)
    ruleSpecificPlayer = Rule(specificPlayerDetails,callback='parse_player', follow=False)

    #ruleNextButton = Rule(next_buttonDetails)
    rules = (ruleAllPlayersDetail,ruleNextDetails,ruleSpecificPlayer)

    custom_settings = {
        'FEED_FORMAT': "csv",
        'FEED_URI': "Newplayers.csv"
    }


    def player_item(self, response):
        yield {
            "playername": response.xpath('//h1[@class="nfl-c-player-header__title"]/text()').get(),
            "Year": response.xpath('//*[@id="main-content"]/section[3]/div/div[4]/div/div[2]/table/tbody/tr/td[1]/text()').getall().split(',') ,
            "Tems Played for": list(set(response.xpath('//table[@summary="Career Stats"]/tbody/tr/td[2]/text()').getall())),
            "G": response.xpath('//table[@summary="Career Stats"]/tbody/tr/td[3]/text()').getall(),
            "GS": response.xpath('//table[@summary="Career Stats"]/tbody/tr/td[4]/text()').getall()
        }

    def parse_player(self,response):

        stasButton = response.xpath('//div[@class="d3-l-col__col-12"]/ul/li[2]/a/@href').get()
        if stasButton is not None:
            yield response.follow(stasButton,callback=self.player_item)
