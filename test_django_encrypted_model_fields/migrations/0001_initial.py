# Generated by Django 3.2.12 on 2022-07-12 15:04

from django.db import migrations, models
import encrypted_model_fields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SampleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plain', models.CharField(blank=True, max_length=100)),
                ('encrypted', encrypted_model_fields.fields.EncryptedCharField(blank=True)),
            ],
        ),
    ]