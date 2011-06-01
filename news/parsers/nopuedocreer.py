import re

from news.parsers import Parser

class Nopuedocreer(Parser):
    def configure(self):
        self.site_url = 'http://www.nopuedocreer.com/'
        self.feed_url = 'http://www.nopuedocreer.com/quelohayaninventado/feed/'
            
    def get_entries(self, content):
        return re.findall('<item>(.*?)</item>', content)
        
    def get_entry_regex(self):
        parts = [
            r'<title>(?P<title>.*?)</title>',
            r'<link>(?P<url>.*?)</link>',
            r'<pubDate>(?P<date>.*?)</pubDate>',
            r'<description>(?P<body>.*?)</description>',
        ]
        return re.compile('(.*?)'.join(parts)) #return
