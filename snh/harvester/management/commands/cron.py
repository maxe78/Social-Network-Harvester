from django.core.management.base import BaseCommand, CommandError
from harvester.models.twitter import *

class Command(BaseCommand):
#    args = '<poll_id poll_id ...>'
#    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        print "hello"
