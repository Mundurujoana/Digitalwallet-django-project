# Generated by Django 4.0.6 on 2022-08-20 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0007_rename_name_account_account_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thirdparty',
            name='phone_Number',
        ),
        migrations.AddField(
            model_name='thirdparty',
            name='phonenumber',
            field=models.CharField(max_length=55, null=True),
        ),
    ]
