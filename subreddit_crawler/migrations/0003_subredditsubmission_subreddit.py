# Generated by Django 2.0 on 2018-01-02 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subreddit_crawler', '0002_subreddit'),
    ]

    operations = [
        migrations.AddField(
            model_name='subredditsubmission',
            name='subreddit',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='subreddit_crawler.Subreddit'),
            preserve_default=False,
        ),
    ]
