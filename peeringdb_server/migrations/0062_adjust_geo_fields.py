# Generated by Django 2.2.17 on 2020-11-30 04:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("peeringdb_server", "0061_update_phone_help_text"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="facility",
            name="geocode_error",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="geocode_error",
        ),
        migrations.AlterField(
            model_name="facility",
            name="geocode_status",
            field=models.BooleanField(
                default=False,
                help_text="Has this object's address been normalized with a call to the Google Maps API",
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="geocode_status",
            field=models.BooleanField(
                default=False,
                help_text="Has this object's address been normalized with a call to the Google Maps API",
            ),
        ),
    ]
