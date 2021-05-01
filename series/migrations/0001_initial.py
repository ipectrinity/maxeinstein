# Generated by Django 3.2 on 2021-05-01 07:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='WebSeries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('visit_url', models.URLField(default='https://youtube.com/')),
                ('no_of_episodes', models.IntegerField(default=1)),
                ('episode_watchtime', models.DurationField(default=datetime.timedelta(seconds=3600))),
                ('genre', models.CharField(max_length=50)),
                ('platform_name', models.CharField(blank=True, default='YouTube', max_length=50)),
                ('platform_url', models.URLField(blank=True, default='https://youtube.com/')),
                ('description', models.TextField(blank=True, default='')),
                ('carousel_images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carousel_images', to='core.seriesimage')),
                ('cover_image', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cover_image', to='core.seriesimage')),
                ('tags', models.ManyToManyField(related_name='series', to='series.Tag')),
            ],
        ),
    ]