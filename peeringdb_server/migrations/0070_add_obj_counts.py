# Generated by Django 2.2.19 on 2021-04-22 22:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("peeringdb_server", "0069_add_ix_service_and_terms"),
    ]

    operations = [
        migrations.AddField(
            model_name="network",
            name="fac_count",
            field=models.PositiveIntegerField(
                default=0,
                help_text="number of facilities at this network",
                verbose_name="number of facilities at this network",
            ),
        ),
        migrations.AddField(
            model_name="network",
            name="ix_count",
            field=models.PositiveIntegerField(
                default=0,
                help_text="number of exchanges at this network",
                verbose_name="number of exchanges at this network",
            ),
        ),
        migrations.AddField(
            model_name="facility",
            name="ix_count",
            field=models.PositiveIntegerField(
                default=0,
                help_text="number of exchanges at this facility",
                verbose_name="number of exchanges at this facility",
            ),
        ),
        migrations.AddField(
            model_name="facility",
            name="net_count",
            field=models.PositiveIntegerField(
                default=0,
                help_text="number of networks at this facility",
                verbose_name="number of networks at this facility",
            ),
        ),
        migrations.AddField(
            model_name="internetexchange",
            name="fac_count",
            field=models.PositiveIntegerField(
                default=0,
                help_text="number of facilities at this exchange",
                verbose_name="number of facilities at this exchange",
            ),
        ),
        migrations.AddField(
            model_name="internetexchange",
            name="net_count",
            field=models.PositiveIntegerField(
                default=0,
                help_text="number of networks at this exchange",
                verbose_name="number of networks at this exchange",
            ),
        ),
    ]
