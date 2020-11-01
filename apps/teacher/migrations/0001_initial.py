# Generated by Django 3.1.1 on 2020-10-31 12:31

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0003_auto_20201029_0622'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(default='default.png', upload_to='teacher')),
                ('teacher_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('designation', models.CharField(max_length=20)),
                ('school_name', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('school_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.school')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]