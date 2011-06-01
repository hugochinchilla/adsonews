import re
import urllib
from  datetime import datetime

from news.models import New

class Parser(object):
    
    def __init__(self):
        self.configure();
        self.entry_regex = self.get_entry_regex()
        self.cdata_regex = re.compile(r'<!\[CDATA\[(.*?)\]\]>')
        
    def configure(self):
        raise Exception('configure is not implemented')
        
    def get_entries(self, content):
        raise Exception('get_entries is not implemented')
        
    def get_entry_regex(self):
        raise Exception('get_entry_regex is not implemented')
        
    def parse_entry(self, new):
        return self.entry_regex.search(new)
        
    def clean_data(self, data):
        """
        Convert a string like "Sun, 29 May 2011 18:55:02 +0000" to
        a valid datetime object.
        """
        data = data.groupdict()
        data['body'] = self.sanitize(data['body'])
        data['date'] = datetime.strptime(data['date'][:-6], '%a, %d %b %Y %H:%M:%S')
        return data        

    def sanitize(self, content):
        cdata = self.cdata_regex.search(content)
        if cdata:
            content = cdata.groups()[0]
        #content = re.sub('<script([^>]*>(.*?)</script>', '', content)
        return content
        
    def get_content(self):
        f = urllib.urlopen(self.feed_url)
        content = f.read()
        f.close()
        return content.replace('\n','')
    
    def import_news(self, limit=10):
        entries = self.get_entries(self.get_content())
        for entry in entries:
            data = self.parse_entry(entry)
            data = self.clean_data(data)
            new = New(**data)
            new.save();
            
