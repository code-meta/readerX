# Generated by Django 4.2.5 on 2023-10-03 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_post_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=models.TextField(blank=True, max_length=320),
        ),
    ]
