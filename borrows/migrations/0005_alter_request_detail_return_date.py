# Generated by Django 3.2 on 2021-04-21 08:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('borrows', '0004_auto_20210421_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request_detail',
            name='return_date',
            field=models.DateField(default=datetime.datetime(2021, 4, 28, 8, 11, 17, 673260, tzinfo=utc)),
        ),
    ]
