from datetime import datetime

from django.contrib.postgres.fields import ArrayField
from django.db import models

from subreddit_crawler.managers import SubredditSubmissionsManager


class Subreddit(models.Model):
    name = models.CharField(max_length=256)
    last_crawled = models.DateTimeField(null=True)


class SubredditSubmission(models.Model):
    id = models.CharField(max_length=128, primary_key=True)
    text = models.TextField()
    subreddit = models.ForeignKey(Subreddit, on_delete=models.CASCADE)

    objects = SubredditSubmissionsManager()


class SearchPhrase(models.Model):
    phrase = models.CharField(max_length=256)
    subreddits = ArrayField(models.CharField(max_length=256))
