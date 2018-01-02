from django.contrib import admin

from subreddit_crawler.models import Subreddit, SubredditSubmission

admin.site.register(Subreddit)
admin.site.register(SubredditSubmission)
