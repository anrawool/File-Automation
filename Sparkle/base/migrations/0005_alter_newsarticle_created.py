# Generated by Django 4.2.3 on 2024-02-18 09:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0004_newsarticle_content_newsarticle_origin_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newsarticle",
            name="created",
            field=models.DateField(null=True),
        ),
    ]
