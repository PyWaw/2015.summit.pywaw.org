import hashlib
from django.core.urlresolvers import reverse
from django.db import models
import uuid
from django.db.models.signals import pre_save
import requests
from . import twitter


def create_attendee_hash():
    while True:
        attendee_hash = uuid.uuid1().hex
        if not Attendee.objects.filter(hash=attendee_hash).exists():
            return attendee_hash


def set_avatar(sender, instance, **kwargs):
    if not instance.avatar:
        email_hash = hashlib.md5(instance.email.lower().encode('utf-8')).hexdigest()
        gravatar_url = "http://www.gravatar.com/avatar/{}?s=150".format(email_hash)
        response = requests.get(gravatar_url, params={'d': 404})

        if response.ok:
            instance.avatar = gravatar_url
        else:
            instance.avatar = twitter.get_twitter_avatar_url(instance.twitter)


class Attendee(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=100)
    email = models.EmailField()
    twitter = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    display_on_website = models.BooleanField(default=True)
    notes = models.TextField(blank=True)
    admin_notes = models.TextField(blank=True)
    invoice = models.BooleanField(default=True)
    company_name = models.CharField(max_length=100, blank=True)
    company_address = models.CharField(max_length=500, blank=True)
    company_post_code = models.CharField(max_length=500, blank=True)
    company_city = models.CharField(max_length=500, blank=True)
    company_nip = models.CharField(max_length=15, blank=True, verbose_name='Company VATIN (NIP)')
    is_paid = models.BooleanField(default=False)
    invoice_sent = models.BooleanField(default=False)
    is_organizer = models.BooleanField(default=False)
    is_speaker = models.BooleanField(default=False)
    is_volunteer = models.BooleanField(default=False)
    registration_date = models.DateTimeField(auto_now_add=True)
    hash = models.CharField(max_length=32, default=create_attendee_hash)
    avatar = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('attendee_detail', kwargs={'hash': self.hash})

    def get_initials(self):
        return ''.join(part[0] for part in self.name.split()).upper()


pre_save.connect(set_avatar, sender=Attendee)
