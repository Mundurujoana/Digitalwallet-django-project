# Generated by Django 4.0.6 on 2022-09-11 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0011_rename_recipt_file_receipts_receipt_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipts',
            name='status',
            field=models.CharField(choices=[('deposits', 'Bank deposits'), ('withdrawals', 'Cash withdrawals'), ('loan', 'loan payments'), ('creditcard', 'creditcard payments')], max_length=15, null=True),
        ),
    ]
