# Generated by Django 4.2.6 on 2023-10-23 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_alter_shop_p_alter_shop_sid'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='address',
            field=models.TextField(default='none'),
        ),
    ]
