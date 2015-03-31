import json
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from django.template.loader import render_to_string
from django.views.generic import CreateView, DetailView
from . import models, forms
import requests


class AttendeeCreateView(CreateView):
    model = models.Attendee
    form_class = forms.AttendeeForm

    def get_success_url(self):
        return self.object.get_absolute_url()

    def form_valid(self, form):
        response = super().form_valid(form)
        self._send_payment_email()
        return response

    def _send_payment_email(self):
        context = {
            'attendee': self.object,
            'site': get_current_site(self.request),
        }
        EmailMessage(
            subject=render_to_string('emails/registration_subject.txt', context).strip(),
            body=render_to_string('emails/registration_body.txt', context),
            from_email=settings.REGISTRATION_EMAIL,
            to=[self.object.email],
            bcc=[settings.REGISTRATION_EMAIL],
        ).send()


class AttendeeDetailView(DetailView):
    model = models.Attendee
    slug_url_kwarg = slug_field = 'hash'


@receiver(post_save, sender=models.Attendee)
def post_to_slack(sender, **kwargs):

    if kwargs['created'] and settings.REGISTRATION_NOTIFICATIONS_URL:
        attendee = kwargs['instance']

        count = models.Attendee.objects.count()

        def post_message(message):
            payload = json.dumps({
                "text": message
            })

            requests.post(
                "https://hooks.slack.com/services/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",
                data=payload)

        post_message(
            "{} ({}) właśnie zarejestrował się na PyWaw Summit!".format(attendee.name, attendee.tagline)
        )
        post_message("Łącznie to już {} zarejesteowanych osób.".format(count))

