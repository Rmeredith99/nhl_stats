# Generated by Django 2.1 on 2019-08-27 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomMetric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('string', models.CharField(max_length=200)),
                ('label', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'CustomMetric',
            },
        ),
        migrations.CreateModel(
            name='CustomStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200)),
                ('value', models.FloatField(null=True)),
                ('username', models.CharField(max_length=200)),
                ('metric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.CustomMetric')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.StatLine')),
            ],
            options={
                'db_table': 'CustomStat',
            },
        ),
    ]
