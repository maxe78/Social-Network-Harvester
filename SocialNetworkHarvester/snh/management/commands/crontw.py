# coding=UTF-8

#import sys
#import os

from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist

from snh.management.commands.cronharvester import twitterch
from snh.management.commands.cronharvester import facebookch

import snhlogger
logger = snhlogger.init_logger(__name__, "twitter.log")

class Command(BaseCommand):
    #args = '<poll_id poll_id ...>'
    #help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        try:
            logger.info("Will run the Twitter harvesters.")
            twitterch.run_twitter_harvester()
        except:
            msg = u"Highest exception for the twitter cron. Not good."
            logger.exception(msg)

        logger.info("The harvest has end for the Twitter harvesters.")



        
