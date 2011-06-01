import re
from news.parsers import Parser

class Meneame(Parser):
    def configure(self):
        self.site_name = 'Meneame'
        self.site_url = 'http://www.meneame.net/'
        self.feed_url = 'http://www.meneame.net/rss2.php'
    
    def get_entries(self, content):
        return re.findall('<item>(.*?)</item>', content)
        
    def get_entry_regex(self):
        parts = [
            r'<meneame:url>(?P<entry_url>.*?)</meneame:url>',
            r'<title>(?P<title>.*?)</title>',
            r'<pubDate>(?P<date>.*?)</pubDate>',
            r'<description>(?P<body>.*?)</description>',
        ]
        return re.compile('(.*?)'.join(parts))