from django.core.urlresolvers import reverse
from django.db import models
import uuid


def create_attendee_hash():
    while True:
        attendee_hash = uuid.uuid1().hex
        if not Attendee.objects.filter(hash=attendee_hash).exists():
            return attendee_hash


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
    registration_date = models.DateTimeField(auto_now_add=True)
    hash = models.CharField(max_length=32, default=create_attendee_hash)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('attendee_detail', kwargs={'hash': self.hash})
