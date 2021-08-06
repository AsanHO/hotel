# Generated by Django 3.2.6 on 2021-08-06 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210806_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cur',
            field=models.CharField(blank=True, choices=[('usd', 'usd'), ('krw', 'krw')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='lan',
            field=models.CharField(blank=True, choices=[('en', 'english'), ('kr', 'korean')], max_length=3, null=True),
        ),
    ]
