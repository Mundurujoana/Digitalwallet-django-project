# Generated by Django 4.0.6 on 2022-08-20 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0009_rename_transaction_cost_thirdparty_transaction_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='status',
            field=models.CharField(choices=[('a', 'active'), ('i', 'inactive')], max_length=50, null=True),
        ),
    ]
