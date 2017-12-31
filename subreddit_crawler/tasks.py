from django.conf import settings
import praw

from subreddit_crawler.celery import app


def create_reddit_client():
    return praw.Reddit(client_id=settings.REDDIT_CLIENT_ID,
                       client_secret=settings.REDDIT_CLIENT_SECRET,
                       user_agent='reddit_crawler for mymo',
                       username=settings.REDDIT_USERNAME,
                       password=settings.REDDIT_PASSWORD)
