# Generated by Django 2.2 on 2021-01-18 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketapp', '0007_auto_20210118_0541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='myuser_choice',
            field=models.CharField(choices=[('A', 'Admin'), ('U', 'User'), ('G', 'Guest'), ('S', 'Seller')], max_length=10),
        ),
    ]