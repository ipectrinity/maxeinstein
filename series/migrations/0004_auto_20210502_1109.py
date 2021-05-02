# Generated by Django 3.2 on 2021-05-02 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0003_auto_20210501_1313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webseries',
            name='cover_image',
        ),
        migrations.AddField(
            model_name='webseries',
            name='cover_image',
            field=models.ImageField(default='', upload_to='images/'),
            preserve_default=False,
        ),
    ]