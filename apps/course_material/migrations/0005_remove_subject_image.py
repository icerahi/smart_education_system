# Generated by Django 3.1.4 on 2020-12-02 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_material', '0004_subject_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='image',
        ),
    ]