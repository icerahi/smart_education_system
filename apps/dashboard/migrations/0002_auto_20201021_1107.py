# Generated by Django 3.1.2 on 2020-10-21 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='district',
        ),
        migrations.RemoveField(
            model_name='school',
            name='division',
        ),
        migrations.RemoveField(
            model_name='union',
            name='upazila',
        ),
        migrations.RemoveField(
            model_name='upazila',
            name='district',
        ),
        migrations.DeleteModel(
            name='District',
        ),
        migrations.DeleteModel(
            name='Division',
        ),
        migrations.DeleteModel(
            name='School',
        ),
        migrations.DeleteModel(
            name='Union',
        ),
        migrations.DeleteModel(
            name='Upazila',
        ),
    ]
