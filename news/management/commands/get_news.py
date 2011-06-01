from django.core.management.base import BaseCommand, CommandError
from adsonews.news.models import New
from adsonews.news.parsers import parsers

class Command(BaseCommand):
    args = ''
    help = 'Get new content from webs'

    def handle(self, *args, **options):
        for parser in parsers:
            p = parser()
            p.import_news()
            
        self.stdout.write('Successfully done nothing\n')
