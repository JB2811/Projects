# Generated by Django 4.2.6 on 2023-10-23 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='pid',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='pname',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='qty',
        ),
        migrations.AddField(
            model_name='shop',
            name='p',
            field=models.CharField(default='unavailable', max_length=1000),
        ),
        migrations.AlterField(
            model_name='shop',
            name='sid',
            field=models.TextField(),
        ),
    ]
