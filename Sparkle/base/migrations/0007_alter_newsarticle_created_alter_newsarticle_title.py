# Generated by Django 4.2.3 on 2024-02-18 10:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0006_newsarticle_created_at_alter_newsarticle_content_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newsarticle",
            name="created",
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="newsarticle",
            name="title",
            field=models.CharField(max_length=200),
        ),
    ]
