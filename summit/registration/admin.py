from django.contrib import admin
from . import models


class AttendeesTypesListFilter(admin.SimpleListFilter):

    title = 'Attendees by type'

    parameter_name = 'attendee_filter'

    def lookups(self, request, model_admin):
        return (
            ('not_paid', 'Registered, not yet paid'),
            ('paid', 'Paid attendees'),
            ('need_invoice', 'Need invoice'),
            ('speakers', 'Speakers'),
            ('organizers', 'Organizers'),
            ('volunteers', 'Volunteers'),
            ('missing_avatar', 'Needs avatar set'),
        )

    def queryset(self, request, queryset):

        filters = {
            'organizers': dict(is_organizer=True),

            'volunteers': dict(is_volunteer=True),

            'speakers': dict(is_speaker=True),

            'paid': dict(is_organizer=False,
                         is_volunteer=False,
                         is_speaker=False,
                         is_paid=True),

            'not_paid': dict(is_organizer=False,
                             is_volunteer=False,
                             is_speaker=False,
                             is_paid=False),

            'need_invoice': dict(is_organizer=False,
                                 is_volunteer=False,
                                 is_speaker=False,
                                 is_paid=True,
                                 invoice_sent=False),

            'missing_avatar': dict(display_on_website=True,
                                   avatar=''),

            None: dict(),
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

    actions = ['mark_as_paid', 'mark_invoice_sent']

    list_filter = (AttendeesTypesListFilter,)

    search_fields = ('name', 'tagline', 'email', 'company_name', 'notes', 'admin_notes')

    def mark_as_paid(self, request, queryset):
        rows_updated = queryset.update(is_paid=True)

        self.message_user(request, "({}) attendees were marked as paid.".format(rows_updated))

    mark_as_paid.short_description = "Marked as paid"

    def mark_invoice_sent(self, request, queryset):
        rows_updated = queryset.update(invoice_sent=True)

        self.message_user(request, "({}) attendees were marked as invoice sent.".format(rows_updated))

    mark_as_paid.marked_invoice_sent = "Mark invoice sent"

admin.site.register(models.Attendee, AttendeeModelAdmin)
