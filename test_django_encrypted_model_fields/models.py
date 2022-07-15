import json
from django.db import models
from django.db import connection
from django.utils.html import linebreaks
from django.utils.safestring import mark_safe
from encrypted_model_fields import fields


class SampleModel(models.Model):
    plain = models.CharField(max_length=100, null=False, blank=True)
    encrypted = fields.EncryptedCharField(max_length=100, null=False, blank=True)
    json_plain = models.JSONField(null=False, blank=True, default=dict)
    json_encrypted = fields.EncryptedJSONField(null=False, blank=True, default=dict)

    def retrieve_raw_field(self, fieldname):
        sql = "select %s from %s_%s where id=%s" % (fieldname, self._meta.app_label, self._meta.model_name, self.id)
        with connection.cursor() as cursor:
            cursor.execute(sql)
            row = cursor.fetchone()
        return row[0]

    def raw_encrypted(self):
        return self.retrieve_raw_field('encrypted')

    def raw_json_encrypted(self):
        return self.retrieve_raw_field('json_encrypted')

    def json_encrypted_then_decoded(self):
        obj = self.json_encrypted
        text = json.dumps(obj, indent=4)
        html = '<pre>' + linebreaks(text) + '</pre>'
        return mark_safe(html)
