# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-06-13 11:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ios_notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='Device',
            name='service',
            field=models.ForeignKey(to='ios_notifications.APNService', on_delete='PROTECTED'),
        ),
        migrations.AlterField(
            model_name='FeedbackService',
            name='service',
            field=models.ForeignKey(to='ios_notifications.APNService', on_delete='PROTECTED'),
        ),
        migrations.AlterField(
            model_name='Notification',
            name='service',
            field=models.ForeignKey(to='ios_notifications.APNService', on_delete='PROTECTED'),
        ),
    ]
