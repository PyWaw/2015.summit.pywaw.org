from django import forms
from . import models
from django.core.exceptions import ValidationError

COMPANY_DETAILS_REQUIRED_ERROR = 'This field is required if you want to receive an invoice.'


class AttendeeForm(forms.ModelForm):
    accept_terms_of_service = forms.BooleanField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs['placeholder'] = field.label

    class Meta:
        model = models.Attendee
        fields = (
            'name',
            'tagline',
            'email',
            'twitter',
            'phone',
            'location',
            'display_on_website',
            'notes',
            'invoice',
            'company_name',
            'company_address',
            'company_post_code',
            'company_city',
            'company_nip',
            'accept_terms_of_service',
        )

    def clean_company_name(self):
        return self._clean_company_field('company_name')

    def clean_company_address(self):
        return self._clean_company_field('company_address')

    def clean_company_post_code(self):
        return self._clean_company_field('company_post_code')

    def clean_company_city(self):
        return self._clean_company_field('company_city')

    def clean_company_nip(self):
        return self._clean_company_field('company_nip')

    def _clean_company_field(self, company_field):
        value = self.cleaned_data[company_field]
        invoice = self.cleaned_data['invoice']
        if invoice and not value:
            raise ValidationError(COMPANY_DETAILS_REQUIRED_ERROR)
        return value