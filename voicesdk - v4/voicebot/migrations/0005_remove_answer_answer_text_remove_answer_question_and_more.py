# Generated by Django 4.2.6 on 2024-08-25 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voicebot', '0004_alter_answer_user_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='answer_text',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.AddField(
            model_name='answer',
            name='answers',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='voicebot.userform'),
        ),
    ]
