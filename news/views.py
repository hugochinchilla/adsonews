from types import UnicodeType

from django.core.paginator import Paginator
from django.db import connection, transaction
from django.db.models import Avg, Max, Min, Count, Q
from django.shortcuts import render_to_response, get_list_or_404, get_object_or_404

from news.models import New


def home(request, page=1):
    try:
        page = int(page)
    except (ValueError, TypeError):
        page = 1
    
    news = New.objects.all()
    pager = Paginator(news, 10)
    pager.current_page = page
    
    context = {
        'pager': pager,
        'results': pager.page(page),
    }
    return render_to_response('news/by_date.html', context)
    
def by_date(request, page=1):
    try:
        page = int(page)
    except (ValueError, TypeError):
        page = 1
    
    news = New.objects.all()
    pager = Paginator(news, 10)
    pager.current_page = page
    
    context = {
        'pager': pager,
        'results': pager.page(page),
    }
    return render_to_response('news/by_date.html', context)
    
def by_source(request, source, page=1):
    try:
        page = int(page)
    except (ValueError, TypeError):
        page = 1
    
    news = New.objects.filter(source_slug=source)
    pager = Paginator(news, 10)
    pager.current_page = page
    
    entry = pager.page(page).object_list[0]
    
    context = {
        'pager': pager,
        'results': pager.page(page),
        'site_name': entry.source_name,
        'site_slug': entry.source_slug,
    }
    return render_to_response('news/by_source.html', context)