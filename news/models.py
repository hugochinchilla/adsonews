from django.db import models

# Create your models here.

class New(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    body = models.TextField()
    entry_url = models.CharField(max_length=255)
    source_name = models.CharField(max_length=255)
    source_url = models.URLField(max_length=255)
    source_slug = models.CharField(max_length=255)
    date = models.DateTimeField()
    imported_at = models.DateTimeField(auto_now_add=True)
    
    class Meta():
        get_latest_by = "date"
        ordering = ['-date']
    

"""
parts = [ 
    r'(?P<vhost>\S+)',                  # vhost %h
    r'(?P<host>\S+)',                   # host %h
    r'\S+',                             # indent %l (unused)
    r'(?P<user>\S+)',                   # user %u
    r'\[(?P<time>.+)\]',                # time %t
    r'"(?P<request>.+)"',               # request "%r"
    r'(?P<status>[0-9]+)',              # status %>s
    r'(?P<size>\S+)',                   # size %b (careful, can be '-')
    r'"(?P<referer>.*)"',               # referer "%{Referer}i"
    r'"(?P<agent>.*)"',                 # user agent "%{User-agent}i"
]

pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')
"""