from django.contrib import admin
from .models import SampleModel


@admin.register(SampleModel)
class SampleModelAdmin(admin.ModelAdmin):
    fields = [
        'plain',
        'encrypted',
        'raw_encrypted',
        'json_plain',
        'json_encrypted',
        'raw_json_encrypted',
        'json_encrypted_then_decoded',
    ]
    readonly_fields = [
        'raw_encrypted',
        'raw_json_encrypted',
        'json_encrypted_then_decoded',
    ]

