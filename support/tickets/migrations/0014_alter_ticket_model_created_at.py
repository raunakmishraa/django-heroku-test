# Generated by Django 4.2.16 on 2024-11-11 17:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0013_alter_ticket_model_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket_model',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 11, 17, 16, 24, 313423, tzinfo=datetime.timezone.utc), verbose_name='Created At'),
        ),
    ]