from django.core.management.base import BaseCommand, CommandError
from help.cadastro_inspiradoras import LeitorCriador

class Command(BaseCommand):
        
    def handle(self, *args, **options):
        cadastrar = LeitorCriador()
        cadastrar.get_user()