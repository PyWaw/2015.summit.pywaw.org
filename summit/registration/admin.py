from django.contrib import admin
from . import models


class AttendeesTypesListFilter(admin.SimpleListFilter):

    title = 'Regular attendees'

    parameter_name = 'attendee_filter'

    def lookups(self, request, model_admin):
        return (
            ('all', 'Attendees without special role'),
            ('payed', 'Payed attendees w/o special role'),
        )

    def queryset(self, request, queryset):
        queryset = queryset.filter(
            is_organizer=False,
            is_speaker=False,
            is_volunteer=False,
        )

        if self.value() == 'payed':
            queryset = queryset.filter(is_payed=True)

        return queryset


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
