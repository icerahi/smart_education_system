# Generated by Django 3.1.1 on 2020-11-02 06:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('course_material', '0003_auto_20201102_0550'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursematerial',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coursematerial',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
