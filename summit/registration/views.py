from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.views.generic import CreateView, DetailView, ListView
from . import models, forms


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


class AttendeesListView(ListView):
    model = models.Attendee
    context_object_name = 'attendees'

    def get_queryset(self):
        return super(AttendeesListView, self).get_queryset().filter(display_on_website=True, is_paid=True).order_by('?')