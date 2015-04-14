from django.contrib import admin
from . import models


class AttendeesTypesListFilter(admin.SimpleListFilter):

    title = 'Attendees by type'

    parameter_name = 'attendee_filter'

    def lookups(self, request, model_admin):
        return (
            ('not_payed', 'Registered, not yet payed'),
            ('payed', 'Payed attendees'),
            ('speakers', 'Speakers'),
            ('organizers', 'Organizers'),
            ('volunteers', 'Volunteers'),
        )

    def queryset(self, request, queryset):

        filters = {
            'organizers': dict(is_organizer=True),

            'volunteers': dict(is_volunteer=True),

            'speakers': dict(is_speaker=True),

            'payed': dict(is_organizer=False,
                          is_volunteer=False,
                          is_speaker=False,
                          is_payed=True),

            'not_payed': dict(is_organizer=False,
                              is_volunteer=False,
                              is_speaker=False,
                              is_payed=True),
        }

        return queryset.filter(**filters[self.value()])


class AttendeeModelAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'location',
        'admin_notes',
        'invoice',
        'is_paid',
        'invoice_sent',
        'registration_date',
    )

    readonly_fields = ('registration_date',)

    actions = ['marked_as_payed', 'marked_invoice_sent']

    list_filter = (
        AttendeesTypesListFilter,
        ('is_speaker', admin.BooleanFieldListFilter),
        ('is_organizer', admin.BooleanFieldListFilter),
        ('is_volunteer', admin.BooleanFieldListFilter),
    )

    def marked_as_payed(self, request, queryset):
        rows_updated = queryset.update(is_paid=True)

        self.message_user(request, "({}) attendees were marked as payed.".format(rows_updated))

    marked_as_payed.short_description = "Marked as payed"

    def marked_invoice_sent(self, request, queryset):
        rows_updated = queryset.update(invoice_sent=True)

        self.message_user(request, "({}) attendees were marked as invoice sent.".format(rows_updated))

    marked_as_payed.short_description = "Mark invoice sent"

admin.site.register(models.Attendee, AttendeeModelAdmin)
