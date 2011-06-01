import re

from news.parsers import Nopuedocreer

class Acampadapalma(Nopuedocreer):
    def configure(self):
        self.site_name = 'Acampada Palma'
        self.site_url = 'http://www.acampadapalma.es/'
        self.feed_url = 'http://www.acampadapalma.es/feed/'
