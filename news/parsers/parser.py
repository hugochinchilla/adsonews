import re
import urllib
from  datetime import datetime

from django.template.defaultfilters import slugify
from django.utils.html import strip_tags

from news.models import New


class Parser(object):
    
    def __init__(self):
        self.site_name = None
        self.site_url = None
        self.site_slug = None
        self.entry_regex = self.get_entry_regex()
        self.cdata_regex = re.compile(r'<!\[CDATA\[(.*?)\]\]>')
        self.configure();
        
    def configure(self):
        raise Exception('configure is not implemented')
        
    def get_entries(self, content):
        raise Exception('get_entries is not implemented')
        
    def get_entry_regex(self):
        raise Exception('get_entry_regex is not implemented')
        
    def parse_entry(self, new):
        match_object = self.entry_regex.search(new)
        data = match_object.groupdict()
        data['source_name'] = self.site_name
        data['source_url'] = self.site_url
        data['source_slug'] = slugify(self.site_name)
        return data
        
    def clean_data(self, data):
        data['title'] = self.sanitize(data['title'])
        data['body'] = self.sanitize(data['body'])
        data['date'] = datetime.strptime(data['date'][:-6], '%a, %d %b %Y %H:%M:%S')
        return data        

    def sanitize(self, content):
        cdata = self.cdata_regex.search(content)
        if cdata:
            content = cdata.groups()[0]
        content = strip_tags(content)
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
            
