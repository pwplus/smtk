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

    def get_redditor_comment_karma(self, names=None):
        """"""
        redditors = self._fetch_redditors_by_name(names=names)

        if redditors: 
            link_karma = [*map(lambda r: r.comment_karma, redditors)]
            return link_karma
        return None

    def get_redditor_comments(self, names=None, limit=10):
        """"""
        redditors = self._fetch_redditors_by_name(names=names)

        if redditors:
            comments = [[comment 
                        for comment in redditor.comments.new(limit=limit)]
                        for redditor in redditors]

            # TODO Discuss whether to return PRAW models or reduced dicts
            # comments = [[*map(lambda c: dict(
            #     author=c.author,
            #     author_flair_text=c.author_flair_text,
            #     body=c.body,
            #     body_html=c.body_html,
            #     edited=c.edited,
            #     gilded=c.gilded,
            #     link_id=c.link_id,
            #     parent_id=c.parent_id,
            #     score=c.score,
            #     score_hidden=c.score_hidden,
            #     subreddit=c.subreddit,
            #     distinguished=c.distinguished
            # ), user_comments)] for user_comments in comments]
            return comments
        return None

    def get_redditor_is_gold(self, names=None):
        """"""
        redditors = self._fetch_redditors_by_name(names=names)

        if redditors:
            is_gold = [*map(lambda r: r.is_gold, redditors)]
            return is_gold
        return None

    def get_redditor_is_mod(self, names=None):
        """"""
        redditors = self._fetch_redditors_by_name(names=names)

        if redditors:
            is_mod = [*map(lambda r: r.is_mod, redditors)]
            return is_mod
        return None

    def get_redditor_link_karma(self, names=None):
        """"""
        redditors = self._fetch_redditors_by_name(names=names)

        if redditors:
            link_karma = [*map(lambda r: r.link_karma, redditors)]
            return link_karma
        return None

    def get_redditor_submissions(self, names=None, limit=10):
        """"""
        redditors = self._fetch_redditors_by_name(names=names)

        # TODO This style = ?
        if redditors:
            submissions = [[submission 
                            for submission
                            in redditor.submissions.new(limit=limit)]
                            for redditor
                            in redditors]

            # TODO Discuss whether to return PRAW models or reduced dicts
            # submissions = [[*map(lambda s: dict(
            #     author=s.author,
            #     author_flair_text=s.author_flair_text,
            #     domain=s.domain,
            #     is_self=s.is_self,
            #     link_flair_text=s.link_flair_text,
            #     locked=s.locked,
            #     num_comments=s.num_comments,
            #     over_18=s.over_18,
            #     permalink=s.permalink,
            #     score=s.score,
            #     selftext=s.selftext,
            #     selftext_html=s.selftext_html,
            #     subreddit=s.subreddit,
            #     thumbnail=s.thumbnail,
            #     title=s.title,
            #     url=s.url,
            #     edited=s.edited,
            #     distinguished=s.distinguished,
            #     stickied=s.stickied
            # ), user_submissions)] for user_submissions in submissions]
            return submissions
        return None

    def _fetch_redditors_by_name(self, names=None):
        """Returns array of praw.models.Redditor"""
        if names:
            redditors = [self.api.redditor(name) for name in names]
            return redditors
        return None
