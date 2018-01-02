import pytest

from subreddit_crawler.models import Subreddit, SubredditSubmission


@pytest.mark.django_db
def test_phrase_count_any_subreddit(subreddit_submission_factory):
    subreddit_submission_factory.create_batch(
        10, text="""Lorem ipsum dolor sit amet, an ius veri choro, sed ut tota nemore eloquentiam. Omnis timeam fierent ius cu. Nec pertinax consequuntur at. At aeterno fabulas ancillae mel, cum vivendo mediocrem ex, has elitr debitis noluisse cu. Ex mel assum gloriatur. Case apeirian necessitatibus quo at.""")

    assert SubredditSubmission.objects.phrase_count('Lorem') == 10


@pytest.mark.django_db
def test_phrase_count_two_subreddits(subreddit_submission_factory):
    subreddit_submission_factory.create_batch(
        10, text="""Lorem ipsum dolor sit amet, an ius veri choro, sed ut tota nemore eloquentiam. Omnis timeam fierent ius cu. Nec pertinax consequuntur at. At aeterno fabulas ancillae mel, cum vivendo mediocrem ex, has elitr debitis noluisse cu. Ex mel assum gloriatur. Case apeirian necessitatibus quo at.""")

    subreddits = Subreddit.objects.values_list('name', flat=True)[:2]

    assert SubredditSubmission.objects.phrase_count(
        'Lorem', subreddits=subreddits) == 2
