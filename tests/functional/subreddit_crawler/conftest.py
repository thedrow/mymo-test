import factory
from pytest_factoryboy import register


@register
class SubredditFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('slug')

    class Meta:
        model = 'subreddit_crawler.Subreddit'


@register
class SubredditSubmissionFactory(factory.django.DjangoModelFactory):
    id = factory.Faker('slug')
    text = factory.Faker('text')
    subreddit = factory.SubFactory(SubredditFactory)

    class Meta:
        model = 'subreddit_crawler.SubredditSubmission'
