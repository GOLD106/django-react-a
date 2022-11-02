# Generated by Django 3.2.16 on 2022-10-14 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InsuranceType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=225)),
                ('imgPath', models.CharField(max_length=225)),
                ('perDayPrice', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UploadInsurance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('insuranceType', models.CharField(max_length=225)),
                ('insurer', models.CharField(max_length=225)),
                ('nif', models.IntegerField()),
                ('citizenCardNum', models.IntegerField()),
                ('citizenCardValidity', models.CharField(max_length=100)),
                ('idCardUpScreen', models.CharField(max_length=200)),
                ('idCardBackScreen', models.CharField(max_length=200)),
                ('userHeloSignData', models.CharField(max_length=100)),
                ('userHeloSignStatus', models.CharField(max_length=100)),
                ('approveStatus', models.CharField(choices=[('ok', 'Ok'), ('pending', 'Pending'), ('failed', 'Failed')], default='pending', max_length=255)),
            ],
        ),
    ]