# Generated by Django 4.1.1 on 2022-09-20 07:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Accounts",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("phone", models.CharField(max_length=12, unique=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("password", models.CharField(max_length=300)),
                ("first_name", models.CharField(max_length=120)),
                ("last_name", models.CharField(max_length=120)),
            ],
        ),
    ]
