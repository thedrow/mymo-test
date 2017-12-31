import pytest
from subreddit_crawler.tasks import create_reddit_client
from django.conf import settings

@pytest.fixture
def mocked_reddit_client(mocker):
    return mocker.patch('subreddit_crawler.tasks.praw.Reddit', autospec=True)

def test_create_reddit_client(mocked_reddit_client):
    create_reddit_client()

    mocked_reddit_client.assert_called_once_with(client_id=settings.REDDIT_CLIENT_ID,
                                                 client_secret=settings.REDDIT_CLIENT_SECRET,
                                                 username=settings.REDDIT_USERNAME,
                                                 password=settings.REDDIT_PASSWORD,
                                                 user_agent='reddit_crawler for mymo')
