# Generated by Django 3.1.1 on 2020-11-16 10:50

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course_material', '0011_delete_historicalcoursematerial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_material.class')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class_routine.day')),
                ('subject', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='class_name', chained_model_field='class_name', on_delete=django.db.models.deletion.CASCADE, to='course_material.subject')),
            ],
            options={
                'ordering': ['start_time'],
            },
        ),
        migrations.AddConstraint(
            model_name='routine',
            constraint=models.UniqueConstraint(fields=('class_name', 'subject', 'day'), name='unique data with class_name subject and day'),
        ),
    ]
