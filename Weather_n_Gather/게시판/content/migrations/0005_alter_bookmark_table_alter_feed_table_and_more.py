# Generated by Django 4.0.1 on 2022-01-26 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_delete_reply_remove_feed_like_count'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='bookmark',
            table='Bookmark',
        ),
        migrations.AlterModelTable(
            name='feed',
            table='Feed',
        ),
        migrations.AlterModelTable(
            name='like',
            table='Like',
        ),
    ]
