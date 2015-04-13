from django.contrib import admin
from . import models


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

    def marked_as_payed(self, request, queryset):
        rows_updated = queryset.update(is_paid=True)

        self.message_user(request, "({}) attendees were marked as payed.".format(rows_updated))

    marked_as_payed.short_description = "Marked as payed"

    def marked_invoice_sent(self, request, queryset):
        rows_updated = queryset.update(invoice_sent=True)

        self.message_user(request, "({}) attendees were marked as invoice sent.".format(rows_updated))

    marked_as_payed.short_description = "Mark invoice sent"

admin.site.register(models.Attendee, AttendeeModelAdmin)
