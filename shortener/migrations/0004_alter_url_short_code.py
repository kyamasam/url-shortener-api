# Generated by Django 4.2.15 on 2024-08-19 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_url_id_alter_url_short_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='short_code',
            field=models.CharField(blank=True, max_length=255, unique=True),
        ),
    ]
