# Generated by Django 4.0.1 on 2022-01-22 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='profile_image',
        ),
        migrations.RemoveField(
            model_name='feed',
            name='user_id',
        ),
        migrations.AddField(
            model_name='feed',
            name='identi',
            field=models.CharField(default=2, max_length=24),
            preserve_default=False,
        ),
    ]
