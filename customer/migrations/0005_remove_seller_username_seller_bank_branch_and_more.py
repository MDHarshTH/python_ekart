# Generated by Django 4.2.6 on 2023-10-13 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_alter_seller_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='username',
        ),
        migrations.AddField(
            model_name='seller',
            name='bank_branch',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='seller',
            name='bank_name',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='seller',
            name='company_name',
            field=models.CharField(default=' ', max_length=30),
        ),
    ]
