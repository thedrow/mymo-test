from django.contrib import admin

from subreddit_crawler.models import (SearchPhrase, Subreddit,
                                      SubredditSubmission)


class SearchPhraseAdmin(admin.ModelAdmin):
    fields = ('phrase', 'subreddits')
    readonly_fields = ('phrase_count',)

    list_display = ('phrase', 'subreddits', 'phrase_count')

    def phrase_count(self, obj):
        return SubredditSubmission.objects.phrase_count(obj.phrase,
                                                        subreddits=obj.subreddits)


admin.site.register(Subreddit)
admin.site.register(SubredditSubmission)
admin.site.register(SearchPhrase, SearchPhraseAdmin)
