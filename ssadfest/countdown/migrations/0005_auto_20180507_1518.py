# Generated by Django 2.0.4 on 2018-05-07 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countdown', '0004_auto_20180422_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]
