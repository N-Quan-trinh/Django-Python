# Generated by Django 3.1.4 on 2021-01-13 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myWeb', '0004_useraccount'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='RealName',
            field=models.CharField(default='N/A', max_length=50),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
    ]
