# Generated by Django 3.1.4 on 2020-12-02 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_material', '0003_coursematerial_unit_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Book Image'),
        ),
    ]
