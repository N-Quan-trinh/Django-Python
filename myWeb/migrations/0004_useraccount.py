# Generated by Django 3.1.4 on 2021-01-13 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myWeb', '0003_game_platform'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=10)),
            ],
        ),
    ]
