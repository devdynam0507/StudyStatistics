# Generated by Django 2.0.3 on 2018-03-30 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userstudydata',
            old_name='korenahour',
            new_name='koreanhour',
        ),
        migrations.AddField(
            model_name='userstudydata',
            name='name',
            field=models.CharField(default='?', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='userstudydata',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
