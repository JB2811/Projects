# Generated by Django 4.2.6 on 2024-09-28 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voicebot', '0006_answer_pdf_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='options',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('MC', 'Multiple Choice'), ('TF', 'True/False'), ('FIB', 'Fill in the Blank'), ('ESSAY', 'Essay')], default='ESSAY', max_length=5),
        ),
    ]
