import json
import requests
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from . import models, constants


@receiver(post_save, sender=models.Attendee)
def post_to_slack(sender, **kwargs):

    if kwargs['created'] and settings.REGISTRATION_NOTIFICATIONS_URL:
        def post_message(message):
            payload = json.dumps({
                'text': message,
            })
            requests.post(
                url=settings.REGISTRATION_NOTIFICATIONS_URL,
                data=payload,
            )

        attendee = kwargs['instance']
        count = models.Attendee.objects.count()
        post_message(constants.NEW_ATTENDEE_SLACK_MESSAGE.format(attendee.name, attendee.tagline))
        post_message(constants.SUMMARY_SLACK_MESSAGE.format(count))
