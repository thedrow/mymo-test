# Generated by Django 2.0.1 on 2018-01-02 20:44

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subreddit_crawler', '0002_searchphrase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchphrase',
            name='subreddits',
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=256), blank=True, size=None),
        ),
        migrations.AlterField(
            model_name='subreddit',
            name='last_crawled',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
