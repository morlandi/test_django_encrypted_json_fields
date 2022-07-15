import json
from django.db import models
from django.db import connection
from django.utils.html import linebreaks
from django.utils.safestring import mark_safe
from encrypted_model_fields import fields


class Key(models.Model):
    updated = models.DateTimeField(auto_now=True)
    value = models.CharField(max_length=64, null=False, blank=False)

    class Meta:
        ordering = ('-updated', )

    def __str__(self):
        return self.value


class SampleModel(models.Model):
    text_encrypted = fields.EncryptedCharField(max_length=100, null=False, blank=True, default="Sample text")
    json_encrypted = fields.EncryptedJSONField(null=False, blank=True, default={
        "str_value": "text",
        "int_value": 123,
        "float_value": 123.45,
        "bool_value": True,
        "list_value": [
            1,
            2,
            "three",
            False,
            5.0
        ],
        "dict_value": {
            "aaa": "AAA",
            "bbb": "BBB",
            "inner": {
                "one": 1,
                "two": 2
            }
        }
    })

    def __str__(self):
        # if self.title:
        #     return self.title
        return str(self.id)

    def retrieve_raw_field(self, fieldname):
        sql = "select %s from %s_%s where id=%s" % (fieldname, self._meta.app_label, self._meta.model_name, self.id)
        with connection.cursor() as cursor:
            cursor.execute(sql)
            row = cursor.fetchone()
        return row[0]

    def raw_text_encrypted(self):
        return self.retrieve_raw_field('text_encrypted')

    def raw_json_encrypted(self):
        return self.retrieve_raw_field('json_encrypted')

    def json_prettified(self):
        obj = self.json_encrypted
        text = json.dumps(obj, indent=4)
        html = '<pre>' + linebreaks(text) + '</pre>'
        return mark_safe(html)
