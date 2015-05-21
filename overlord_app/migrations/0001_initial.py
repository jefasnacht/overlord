# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_text', models.CharField(max_length=200)),
                ('lat', models.IntegerField(default=0)),
                ('lon', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_name', models.CharField(max_length=200)),
                ('discover_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='feature',
            field=models.ForeignKey(to='overlord_app.Feature'),
        ),
    ]
