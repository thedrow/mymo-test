from unittest import mock

import pytest
from django.conf import settings

from subreddit_crawler.tasks import create_reddit_client, scrape_subreddit


@pytest.fixture
def mocked_reddit_client(mocker):
    return mocker.patch('subreddit_crawler.tasks.praw.Reddit')


@pytest.fixture
def mocked_subreddit_submission(mocker):
    return mocker.patch('subreddit_crawler.tasks.SubredditSubmission', autospec=True)


@pytest.fixture(scope='session')
def subreddit(faker):
    return faker.slug()


@pytest.fixture(scope='session')
def start_date(faker):
    return faker.unix_time()


def test_create_reddit_client(mocked_reddit_client):
    create_reddit_client()

    mocked_reddit_client.assert_called_once_with(client_id=settings.REDDIT_CLIENT_ID,
                                                 client_secret=settings.REDDIT_CLIENT_SECRET,
                                                 username=settings.REDDIT_USERNAME,
                                                 password=settings.REDDIT_PASSWORD,
                                                 user_agent='reddit_crawler for mymo')


def test_scrape_subreddit_no_new_submissions(mocked_reddit_client,
                                             mocked_subreddit_submission,
                                             subreddit,
                                             start_date):
    scrape_subreddit(subreddit, start_date=start_date)

    mocked_reddit_client().subreddit.assert_called_once_with(subreddit)
    mocked_reddit_client().subreddit().submissions.assert_called_once_with(start=start_date,
                                                                           end=None)
    assert not mocked_subreddit_submission.objects.bulk_create.called


def test_scrape_subreddit_insert_new_submissions(mocked_reddit_client,
                                                 mocked_subreddit_submission,
                                                 subreddit,
                                                 start_date):
    submission1 = mock.Mock()
    submission2 = mock.Mock()
    mocked_reddit_client().subreddit().submissions.return_value = [submission1,
                                                                   submission2]
    mocked_reddit_client().subreddit.reset_mock()

    scrape_subreddit(subreddit, start_date=start_date)

    mocked_reddit_client().subreddit.assert_called_once_with(subreddit)
    mocked_reddit_client().subreddit().submissions.assert_called_once_with(start=start_date,
                                                                           end=None)
    mocked_subreddit_submission.objects.bulk_create.assert_called_once_with([
        mocked_subreddit_submission(
            id=submission1.id, text=submission1.selftext),
        mocked_subreddit_submission(
            id=submission2.id, text=submission2.selftext)
    ])
