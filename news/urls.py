from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from news import views

urlpatterns = patterns('',
    url('^$',
        views.home,
        name='news_home'
    ),
    url('^noticias/(?P<page>\w|\d+)?$',
        views.by_date,
        name='news_by_date'
    ),
)