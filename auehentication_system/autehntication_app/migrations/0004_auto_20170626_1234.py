# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autehntication_app', '0003_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(max_length=500, upload_to=b'C:\\Users\\jaymishr\\DjangoProject\\AuthenticationSystem\\auehentication_system\\static\\images', blank=True),
        ),
    ]
