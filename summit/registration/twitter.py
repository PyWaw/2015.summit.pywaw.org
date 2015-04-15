from django.conf import settings
import logging
import tweepy

logger = logging.getLogger(__name__)


def get_twitter_avatar_url(twitter_id):
    try:
        auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY,
                                   settings.TWITTER_CONSUMER_SECRET)
        auth.set_access_token(settings.TWITTER_ACCESS_TOKEN,
                              settings.TWITTER_ACCESS_TOKEN_SECRET)

        api = tweepy.API(auth)

        user = api.get_user(twitter_id)

        return user.profile_image_url.replace('_normal', '')

    except Exception as e:
        logger.warn("Failed to load Twitter avatar due to {}".format(e.args))
        return ''
