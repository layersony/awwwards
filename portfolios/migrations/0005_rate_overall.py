# Generated by Django 2.1 on 2021-07-18 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0004_auto_20210718_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='overall',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
