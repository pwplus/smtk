import praw
from smtk.utils import helpers
import logging

logging.basicConfig(format='%(asctime)s %(name)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class CollectReddit:

    def __init__(self, stream=True):
        self.auth = helpers.reddit_auth()
        self.api = praw.Reddit(**self.auth)
        self.stream = stream

    def on_redditor(self, redditor):
        """ Called when redditor (user) is found """
        pass

    def get_link_karma(self, names=None):
        """"""
        redditors = _fetch_redditors_by_name(names=names)

        if redditors:
            link_karma = map(lambda r: r.link_karma, redditors)
            return link_karma

        return None

    def _fetch_redditors_by_name(self, names=None):
        """"""
        if names:
            redditors = [self.api.redditor(name) for name in names]
            return redditors;
        return None;
