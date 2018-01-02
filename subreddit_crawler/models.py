from datetime import datetime

from django.db import models


class Subreddit(models.Model):
    name = models.CharField(max_length=256)
    last_crawled = models.DateTimeField(null=True)


class SubredditSubmission(models.Model):
    id = models.CharField(max_length=128, primary_key=True)
    text = models.TextField()
    subreddit = models.ForeignKey(Subreddit, on_delete=models.CASCADE)
