# Generated by Django 3.1.1 on 2020-11-01 06:15

import apps.course_material.models
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_material.class')),
            ],
        ),
        migrations.CreateModel(
            name='CourseMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.FileField(upload_to=apps.course_material.models.content_file_name)),
                ('chapter_name', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='subject_name', chained_model_field='subject_name', on_delete=django.db.models.deletion.CASCADE, to='course_material.chapter')),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_material.class')),
                ('subject_name', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='class_name', chained_model_field='class_name', on_delete=django.db.models.deletion.CASCADE, to='course_material.subject')),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='class_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_material.class'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='subject_name',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='class_name', chained_model_field='class_name', on_delete=django.db.models.deletion.CASCADE, to='course_material.subject'),
        ),
    ]
