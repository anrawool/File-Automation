# Generated by Django 4.2.3 on 2024-02-18 10:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0008_alter_newsarticle_origin"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newsarticle",
            name="title",
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
