# Generated by Django 3.2.13 on 2022-04-12 15:54

import django.core.validators
import django_inet.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("peeringdb_server", "0082_api_throttle_msg"),
    ]

    operations = [
        migrations.AlterField(
            model_name="environmentsetting",
            name="setting",
            field=models.CharField(
                choices=[
                    ("API_THROTTLE_RATE_ANON", "API: Anonymous API throttle rate"),
                    ("API_THROTTLE_RATE_USER", "API: Authenticated API throttle rate"),
                    (
                        "API_THROTTLE_MELISSA_RATE_USER",
                        "API: Melissa request throttle rate for users",
                    ),
                    (
                        "API_THROTTLE_MELISSA_ENABLED_USER",
                        "API: Melissa request throttle enabled for users",
                    ),
                    (
                        "API_THROTTLE_MELISSA_RATE_ORG",
                        "API: Melissa request throttle rate for organizations",
                    ),
                    (
                        "API_THROTTLE_MELISSA_ENABLED_ORG",
                        "API: Melissa request throttle enabled for organizations",
                    ),
                    (
                        "API_THROTTLE_MELISSA_RATE_IP",
                        "API: Melissa request throttle rate for anonymous requests (ips)",
                    ),
                    (
                        "API_THROTTLE_MELISSA_ENABLED_IP",
                        "API: Melissa request throttle enabled for anonymous requests (ips)",
                    ),
                    (
                        "API_THROTTLE_RESPONSE_SIZE_THRESHOLD_CIDR",
                        "API: Response size throttle size threshold for ip blocks (bytes)",
                    ),
                    (
                        "API_THROTTLE_RESPONSE_SIZE_RATE_CIDR",
                        "API: Response size throttle rate for ip blocks",
                    ),
                    (
                        "API_THROTTLE_RESPONSE_SIZE_ENABLED_CIDR",
                        "API: Response size throttle enabled for ip blocks",
                    ),
                    (
                        "API_THROTTLE_RESPONSE_SIZE_THRESHOLD_IP",
                        "API: Response size throttle size threshold for ip addresses (bytes)",
                    ),
                    (
                        "API_THROTTLE_RESPONSE_SIZE_RATE_IP",
                        "API: Response size throttle rate for ip addresses",
                    ),
                    (
                        "API_THROTTLE_RESPONSE_SIZE_ENABLED_IP",
                        "API: Response size throttle enabled for ip addresses",
                    ),
                    (
                        "API_THROTTLE_RESPONSE_SIZE_THRESHOLD_USER",
                        "API: Response size throttle size threshold for authenticated users (bytes)",
                    ),
                    (
                        "API_THROTTLE_RESPONSE_SIZE_RATE_USER",
                        "API: Response size throttle rate for authenticated users",
                    ),
                    (
                        "API_THROTTLE_RESPONSE_SIZE_ENABLED_USER",
                        "API: Response size throttle enabled for authenticated users",
                    ),
                    (
                        "API_THROTTLE_RESPONSE_SIZE_THRESHOLD_ORG",
                        "API: Response size throttle size threshold for organization api-keys (bytes)",
                    ),
                    (
                        "API_THROTTLE_RESPONSE_SIZE_RATE_ORG",
                        "API: Response size throttle rate for organization api-keys",
                    ),
                    (
                        "API_THROTTLE_RESPONSE_SIZE_ENABLED_ORG",
                        "API: Response size throttle enabled for organization api-keys",
                    ),
                    (
                        "API_THROTTLE_RATE_ANON_MSG",
                        "API: Anonymous API throttle rate message",
                    ),
                    (
                        "API_THROTTLE_RATE_USER_MSG",
                        "API: Authenticated API throttle rate message",
                    ),
                ],
                max_length=255,
                unique=True,
            ),
        ),
    ]
