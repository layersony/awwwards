# Generated by Django 2.1 on 2021-07-19 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0005_rate_overall'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profilePic',
            field=models.ImageField(blank=True, default='userProfile/test.png', null=True, upload_to='userProfile/'),
        ),
    ]
