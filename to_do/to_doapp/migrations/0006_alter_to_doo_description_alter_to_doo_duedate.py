# Generated by Django 4.0.2 on 2022-07-16 11:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_doapp', '0005_alter_to_doo_duedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='to_doo',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='to_doo',
            name='duedate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 16, 17, 2, 9, 307024)),
        ),
    ]