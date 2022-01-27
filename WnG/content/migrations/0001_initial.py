# Generated by Django 2.2.5 on 2022-01-27 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_id', models.IntegerField(default=0)),
                ('identi', models.CharField(max_length=24)),
                ('is_marked', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Bookmark',
            },
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('image', models.TextField()),
                ('identi', models.CharField(max_length=24)),
            ],
            options={
                'db_table': 'Feed',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_id', models.IntegerField(default=0)),
                ('identi', models.CharField(max_length=24)),
                ('is_like', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Like',
            },
        ),
    ]
