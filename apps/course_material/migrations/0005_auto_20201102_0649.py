# Generated by Django 3.1.1 on 2020-11-02 06:49

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('course_material', '0004_auto_20201102_0639'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chapter',
            old_name='_class',
            new_name='class_name',
        ),
        migrations.RenameField(
            model_name='coursematerial',
            old_name='_class',
            new_name='class_name',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='_class',
            new_name='class_name',
        ),
        migrations.AlterField(
            model_name='coursematerial',
            name='subject',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='class_name', chained_model_field='class_name', on_delete=django.db.models.deletion.CASCADE, to='course_material.subject'),
        ),
    ]
