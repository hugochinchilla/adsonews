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