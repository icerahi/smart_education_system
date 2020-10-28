# Generated by Django 3.1.2 on 2020-10-28 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0002_auto_20201025_0736'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(default='default.png', upload_to='teacher')),
                ('teacher_id', models.AutoField(primary_key=True, serialize=False)),
                ('designation', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('school_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.school')),
            ],
        ),
    ]
