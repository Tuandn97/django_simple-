# Generated by Django 4.2 on 2024-06-12 04:37

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Chat",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "chat_history",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(), size=None
                    ),
                ),
                ("gpt_model", models.CharField(max_length=100)),
                ("character", models.CharField(max_length=100)),
            ],
        ),
    ]
