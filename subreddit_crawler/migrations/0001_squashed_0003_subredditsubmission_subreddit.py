# Generated by Django 2.0 on 2018-01-02 14:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('subreddit_crawler', '0001_initial'), ('subreddit_crawler',
                                                        '0002_subreddit'), ('subreddit_crawler', '0003_subredditsubmission_subreddit')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubredditSubmission',
            fields=[
                ('id', models.CharField(max_length=128,
                                        primary_key=True, serialize=False)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Subreddit',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('last_crawled', models.DateTimeField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='subredditsubmission',
            name='subreddit',
            field=models.ForeignKey(
                default=0, on_delete=django.db.models.deletion.CASCADE, to='subreddit_crawler.Subreddit'),
            preserve_default=False,
        ),
    ]
