# Generated by Django 3.1.1 on 2020-11-10 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0005_auto_20201109_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notice',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]