from datetime import datetime

from django.db import models


class SubredditSubmission(models.Model):
    id = models.CharField(max_length=128, primary_key=True)
    text = models.TextField()


class Subreddit(models.Model):
    name = models.CharField(max_length=256)
    last_crawled = models.DateTimeField(null=True)
