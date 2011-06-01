import re
import urllib

from news.models import New

class Parser(object):
    
    def __init__(self):
        self.configure();
        self.entry_regex = self.get_entry_regex()
        
    def configure(self):
        raise Exception('configure is not implemented')
        
    def get_entries(self, content):
        raise Exception('get_entries is not implemented')
        
    def get_entry_regex(self):
        raise Exception('get_entry_regex is not implemented')
        
    def parse_entry(self, new):
        return self.entry_regex.search(new)
        
    def clean_data(self, data):
        return data.groupdict();
        
    def get_content(self):
        f = urllib.urlopen(self.feed_url)
        content = f.read()
        f.close()
        return content.replace('\n','')
        
    def sanitize(self, content):
        return content
    
    def import_news(self, limit=10):
        entries = self.get_entries(self.get_content())
        for entry in entries:
            data = self.parse_entry(entry)
            data = self.clean_data(data)
            new = New(**data)
            new.save();
            
