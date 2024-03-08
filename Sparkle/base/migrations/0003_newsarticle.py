# Generated by Django 4.2.3 on 2024-02-18 08:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0002_room_host_message"),
    ]

    operations = [
        migrations.CreateModel(
            name="NewsArticle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True, null=True)),
                ("created", models.DateField(auto_now_add=True)),
            ],
        ),
    ]
