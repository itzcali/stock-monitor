# Generated by Django 2.0.8 on 2018-12-24 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0006_merge_20181202_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='average_volume',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='market_cap',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='share_volume',
            field=models.FloatField(null=True),
        ),
    ]
