# Generated by Django 3.2 on 2021-05-01 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0002_alter_webseries_options'),
        ('users', '0002_alter_viewer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewer',
            name='completed',
            field=models.ManyToManyField(blank=True, related_name='completed', to='series.WebSeries'),
        ),
        migrations.AlterField(
            model_name='viewer',
            name='favorites',
            field=models.ManyToManyField(blank=True, related_name='favorites', to='series.WebSeries'),
        ),
        migrations.AlterField(
            model_name='viewer',
            name='watchlist',
            field=models.ManyToManyField(blank=True, related_name='watched', to='series.WebSeries'),
        ),
    ]