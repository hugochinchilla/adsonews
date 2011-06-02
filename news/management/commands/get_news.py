from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError

from adsonews.news.models import New
from adsonews.news.parsers import parsers

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

class Command(BaseCommand):
    args = ''
    help = 'Get new content from webs'

    def handle(self, *args, **options):
        for parser in parsers:
            p = parser()
            news = p.extract_entries()
            for new in news:
                self.load_entry(new)
        
        self.stdout.write(blue('All done, have a nice day :)\n'))

    def load_entry(self, data):
        try:
            new = New(**data)
            new.save();
            self.stdout.write("%s %s\n" % (green('Nueva noticia:'), new.title))
        except IntegrityError, e:
            self.stdout.write("%s %s\n" % (orange('Noticia duplicada:'), new.title))
        except:
            self.stdout.write("%s %s\n" % (red('Error cargando noticia:'), new.title))
