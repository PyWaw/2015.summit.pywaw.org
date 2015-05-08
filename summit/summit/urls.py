from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.views.generic import TemplateView
from registration.views import AttendeeCreateView, AttendeeDetailView, AttendeesListView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^code-of-conduct/$', TemplateView.as_view(template_name='code_of_conduct.html'), name='code-of-conduct'),
    url(r'^accommodation/$', TemplateView.as_view(template_name='accommodation.html'), name='accommodation'),
    url(r'^registration/$', AttendeeCreateView.as_view(), name='attendee_create'),
    url(r'^registration/(?P<hash>[\w-]+)/$', AttendeeDetailView.as_view(), name='attendee_detail'),
    url(r'^attendees/$', AttendeesListView.as_view(), name='attendee_list'),
    url(r'^speakers-guide/$', TemplateView.as_view(template_name='speakers_guide.html'), name='speakers-guide'),
    url(r'^admin/', include(admin.site.urls)),
)
