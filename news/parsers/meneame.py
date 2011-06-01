import re
from  datetime import datetime
from news.parsers import Parser

class Meneame(Parser):
    def configure(self):
        self.site_url = 'http://www.meneame.net/'
        self.feed_url = 'http://www.meneame.net/rss2.php'
        
    """
    def get_content(self):
        f = open('/home/hugo/Escritorio/meneame_feed.xml')
        data = f.read().replace('\n','')
        f.close()
        return data
    """
    
    def get_entries(self, content):
        return re.findall('<item>(.*?)</item>', content)
        
    def get_entry_regex(self):
        parts = [
            r'<meneame:url>(?P<url>.*?)</meneame:url>',
            r'<title>(?P<title>.*?)</title>',
            r'<pubDate>(?P<date>.*?)</pubDate>',
            r'<description>(?P<body>.*?)</description>',
        ]
        return re.compile('(.*?)'.join(parts))
        
    def clean_data(self, data):
        """
        Convert a string like "Sun, 29 May 2011 18:55:02 +0000" to
        a valid datetime object.
        """
        data = super(Meneame, self).clean_data(data);
        data['date'] = datetime.strptime(data['date'][:-6], '%a, %d %b %Y %H:%M:%S')
        return data