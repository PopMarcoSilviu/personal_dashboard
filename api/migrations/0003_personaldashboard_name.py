# Generated by Django 3.2.8 on 2021-12-07 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211204_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldashboard',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
