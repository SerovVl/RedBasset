import time

from tests.conftest import podcaster


def test_deleting_author(creating_author):
    podcaster.author_settings()
    podcaster.delete_author()
    time.sleep(11)