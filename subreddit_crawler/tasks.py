import praw
from django.conf import settings

from subreddit_crawler.celery import app
from subreddit_crawler.models import SubredditSubmission


def create_reddit_client():
    return praw.Reddit(client_id=settings.REDDIT_CLIENT_ID,
                       client_secret=settings.REDDIT_CLIENT_SECRET,
                       user_agent='reddit_crawler for mymo',
                       username=settings.REDDIT_USERNAME,
                       password=settings.REDDIT_PASSWORD)


@app.task
def scrape_subreddit(subreddit_name, start_date, end_date=None):
    reddit_client = create_reddit_client()

    submissions = [
        SubredditSubmission(id=submission.id,
                            text=submission.selftext)
        for submission in reddit_client.subreddit(subreddit_name).submissions(start=start_date,
                                                                              end=end_date)
    ]
    if submissions:
        SubredditSubmission.objects.bulk_create(submissions)
