# Generated by Django 3.1.1 on 2020-11-02 05:50

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('course_material', '0002_auto_20201102_0535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursematerial',
            name='chapter',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='subject', chained_model_field='subject', on_delete=django.db.models.deletion.CASCADE, to='course_material.chapter', unique=True),
        ),
    ]