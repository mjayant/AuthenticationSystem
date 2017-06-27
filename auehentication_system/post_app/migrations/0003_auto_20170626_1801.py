# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0002_auto_20170626_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 26, 12, 31, 21, 978000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 26, 12, 31, 32, 335000, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
