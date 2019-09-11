# Generated by Django 2.1 on 2019-08-28 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0004_auto_20190828_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customstat',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom_stat_player', to='stats.StatLine'),
        ),
    ]