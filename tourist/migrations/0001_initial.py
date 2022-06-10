# Generated by Django 3.2.6 on 2022-06-08 10:33

import datetime
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='touristguideform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guide_name', models.CharField(max_length=30, null=True)),
                ('business_address', models.CharField(max_length=100, null=True)),
                ('residential_address', models.CharField(max_length=100, null=True)),
                ('year_of_establishment', models.DateField(default=datetime.date.today)),
                ('telephone_number', models.IntegerField(null=True)),
                ('residential_number', models.IntegerField(null=True)),
                ('telegraphic_address', models.CharField(max_length=100, null=True)),
                ('educational_qualifications', models.CharField(max_length=30, null=True)),
                ('year_of_experiance', models.IntegerField(null=True)),
                ('number_of_languages', models.IntegerField(null=True)),
                ('no_training', models.BooleanField(default=False)),
                ('training_Institute_Name', models.CharField(max_length=30, null=True)),
                ('start_Date', models.DateField(default=datetime.date.today)),
                ('end_Date', models.DateField(default=datetime.date.today)),
                ('bank_name', models.CharField(max_length=30, null=True)),
                ('capital_invested', models.IntegerField(null=True)),
                ('terms', multiselectfield.db.fields.MultiSelectField(choices=[('Whether any other activities are proposed to be undertaken? If so, in what fields?', 'Whether any other activities are proposed to be undertaken? If so, in what fields?'), ('Please state if you or your partner, if anyone have been convicted of an offence, if so please give details.', 'Please state if you or your partner, if anyone have been convicted of an offence, if so please give details.'), ('I/we hereby solemnly declare that all the particulars give above are correct', 'I/we hereby solemnly declare that all the particulars give above are correct'), ('I/we hereby solemnly declare that if a licence is granted to me/us, I/We will abide by the Travel Agencies Act, 1976 and the Rules made their under the terms of the licence granted to me/us, and the code of conduct.', 'I/we hereby solemnly declare that if a licence is granted to me/us, I/We will abide by the Travel Agencies Act, 1976 and the Rules made their under the terms of the licence granted to me/us, and the code of conduct.')], max_length=484, null=True)),
            ],
        ),
    ]
