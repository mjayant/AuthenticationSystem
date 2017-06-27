# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autehntication_app', '0002_auto_20170617_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(upload_to=b'C:\\Users\\jaymishr\\DjangoProject\\AuthenticationSystem\\auehentication_system\\static\\images', blank=True),
        ),
    ]
