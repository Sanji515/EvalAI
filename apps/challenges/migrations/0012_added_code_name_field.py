# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-22 00:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("challenges", "0011_approved_by_admin_field_added")]

    operations = [
        migrations.AddField(
            model_name="challengephase",
            name="code_name",
            field=models.CharField(default="Phase Code Name", max_length=100),
        )
    ]
