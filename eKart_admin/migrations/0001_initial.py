# Generated by Django 4.2.6 on 2023-11-13 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('discription', models.CharField(max_length=200)),
                ('cover_picture', models.ImageField(upload_to='category/')),
            ],
            options={
                'db_table': 'category_tb',
            },
        ),
        migrations.CreateModel(
            name='EkartAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'admin_tb',
            },
        ),
    ]
