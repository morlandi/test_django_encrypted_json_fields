from django.contrib import admin
from django.conf import settings
from .models import Key
from .models import SampleModel


@admin.register(Key)
class KeyAdmin(admin.ModelAdmin):
    pass


@admin.register(SampleModel)
class SampleModelAdmin(admin.ModelAdmin):

    readonly_fields = [
        'raw_text_encrypted',
        'raw_json_encrypted',
        'json_prettified',
    ]

    def get_fields(self, request, obj=None):
        if obj is None or not settings.SHOW_RAW_FIELDS:
            fields = [
                'text_encrypted',
                'json_encrypted',
            ]
        else:
            fields = [
                ('text_encrypted', 'raw_text_encrypted', ),
                ('json_encrypted', 'json_prettified', 'raw_json_encrypted', ),

            ]
        return fields
