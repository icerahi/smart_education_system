# Generated by Django 3.1.2 on 2020-10-25 07:21

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='District')),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Division')),
            ],
        ),
        migrations.CreateModel(
            name='Upazila',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Upazila')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.district')),
            ],
        ),
        migrations.CreateModel(
            name='Union',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Union')),
                ('upazila', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.upazila')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('name', models.CharField(max_length=300)),
                ('school_id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField()),
                ('village', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('district', smart_selects.db_fields.ChainedForeignKey(chained_field='division', chained_model_field='division', on_delete=django.db.models.deletion.CASCADE, to='school.district')),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.division')),
                ('union', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.union')),
                ('upazila', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.upazila')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='district',
            name='division',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.division'),
        ),
    ]