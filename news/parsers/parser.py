import re
import urllib
import HTMLParser
from  datetime import datetime

from django.template.defaultfilters import slugify
from django.utils.html import strip_tags

from news.models import New

_HEADER = '\033[95m'
_OKBLUE = '\033[94m'
_OKGREEN = '\033[92m'
_WARNING = '\033[93m'
_FAIL = '\033[91m'
_ENDC = '\033[0m'

green = lambda x: _OKGREEN + x + _ENDC
blue = lambda x: _OKBLUE + x + _ENDC
orange = lambda x: _WARNING + x + _ENDC
red = lambda x: _FAIL + x + _ENDC

class Parser(object):
    
    def __init__(self):
        self.html_parser = HTMLParser.HTMLParser()
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
        
    def get_content(self):
        f = urllib.urlopen(self.feed_url)
        content = f.read()
        f.close()
        return content.replace('\n','')
        
    def extract_entries(self, limit=10):
        entries = self.get_entries(self.get_content())
        return [self.parse_entry(entry) for entry in entries]
        
    def parse_entry(self, new):
        match_object = self.entry_regex.search(new)
        data = match_object.groupdict()
        data['source_name'] = self.site_name
        data['source_url'] = self.site_url
        data['source_slug'] = slugify(self.site_name)
        return self.clean_data(data)
        
    def clean_data(self, data):
        data['title'] = self.clean_title(data['title'])
        data['body'] = self.clean_body(data['body'])
        data['date'] = self.clean_date(data['date'])
        return data
    
    def clean_date(self, string):
        return datetime.strptime(string[:-6], '%a, %d %b %Y %H:%M:%S')
        
    def clean_body(self, string):
        return self.sanitize(string)
        
    def clean_title(self, string):
        return self.sanitize(string)

    def sanitize(self, content):
        cdata = self.cdata_regex.search(content)
        if cdata:
            content = cdata.groups()[0]
        content = strip_tags(content)
        content = self.html_parser.unescape(content)
        return content
