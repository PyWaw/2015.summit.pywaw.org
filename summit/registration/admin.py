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

admin.site.register(models.Attendee, AttendeeModelAdmin)
