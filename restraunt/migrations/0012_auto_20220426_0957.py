# Generated by Django 3.2 on 2022-04-26 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restraunt', '0011_auto_20220426_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='restraunt',
            name='address',
            field=models.TextField(default=1, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='restraunt',
            name='telegraphic_num',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AddField(
            model_name='restraunt',
            name='telephone_num',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
