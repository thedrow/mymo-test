from django.db.models import F, Func, Manager, Sum, Value


class SubredditSubmissionsManager(Manager):
    def phrase_count(self, phrase, subreddits=None):
        qs = self.get_queryset()

        if subreddits:
            qs = qs.filter(subreddit__name__in=subreddits)

        result = qs.aggregate(phrase_count=Sum((Func(F('text'), function='CHAR_LENGTH') - Func(Func(
            F('text'), Value(phrase), Value(''), function='REPLACE'), function='CHAR_LENGTH')) / Value(len(phrase))))

        return result['phrase_count']
