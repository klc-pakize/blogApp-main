# Generated by Django 4.1.7 on 2023-02-24 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.CharField(blank=True, choices=[('d', 'Draft'), ('p', 'Published')], default='d', max_length=5, null=True),
        ),
    ]
