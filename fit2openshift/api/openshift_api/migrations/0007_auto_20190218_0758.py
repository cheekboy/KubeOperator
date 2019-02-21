# Generated by Django 2.1.2 on 2019-02-18 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openshift_api', '0006_auto_20190218_0750'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='cpu_core',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='node',
            name='memory',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='node',
            name='os',
            field=models.CharField(default='unknown', max_length=128),
        ),
    ]