# Generated by Django 4.0.2 on 2022-07-27 06:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_doapp', '0008_todolist_alter_to_doo_duedate_to_doo_todo_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='to_doo',
            name='duedate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 27, 12, 5, 6, 344966)),
        ),
    ]