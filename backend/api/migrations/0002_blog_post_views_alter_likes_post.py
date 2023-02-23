# Generated by Django 4.1.7 on 2023-02-23 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='post_views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='likes',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_n', to='api.blog'),
        ),
    ]