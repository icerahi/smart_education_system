# Generated by Django 3.1.4 on 2020-12-09 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('node', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=20)),
                ('single_group', models.CharField(max_length=30)),
                ('channel_name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('node', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='node.node')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]