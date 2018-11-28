# Generated by Django 2.0.2 on 2018-11-18 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_auto_20181117_1543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='id',
        ),
        migrations.AddField(
            model_name='stock',
            name='symbol',
            field=models.CharField(default='temp', max_length=5, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stock',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]