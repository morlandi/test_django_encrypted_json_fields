from django.contrib import admin
from .models import SampleModel


@admin.register(SampleModel)
class SampleModelAdmin(admin.ModelAdmin):
    pass

    readonly_fields = [
        'raw_encrypted',
        'raw_json_encrypted',
    ]
