# Generated by Django 3.2.6 on 2022-06-07 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourist', '0006_auto_20220607_1207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='touristguideform',
            name='bank_name',
        ),
        migrations.RemoveField(
            model_name='touristguideform',
            name='capital_invested',
        ),
        migrations.RemoveField(
            model_name='touristguideform',
            name='end_Date',
        ),
        migrations.RemoveField(
            model_name='touristguideform',
            name='start_Date',
        ),
        migrations.RemoveField(
            model_name='touristguideform',
            name='terms',
        ),
        migrations.RemoveField(
            model_name='touristguideform',
            name='training_Institute_Name',
        ),
    ]
