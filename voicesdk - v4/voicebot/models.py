from django.db import models
from django.contrib.postgres.fields import JSONField  # For PostgreSQL
# from django.db.models import JSONField  # For Django 3.1+ and PostgreSQL

class UserForm(models.Model):
    name = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=255)

class Question(models.Model):
    QUESTION_TYPE_CHOICES = [('MC', 'Multiple Choice'),('TF', 'True/False'),('FIB','Fill in the Blank'),('ESSAY','Essay')]
    question_text = models.TextField()
    question_type = models.CharField(max_length=5, choices=QUESTION_TYPE_CHOICES, default='ESSAY')
    options = models.JSONField(blank=True, null=True)

class Answer(models.Model):
    user = models.OneToOneField(UserForm, on_delete=models.CASCADE)  # Ensure one row per user
    answers = models.JSONField(default=dict)  # Store answers as a JSON object
    pdf_file = models.FileField(upload_to='exam_results/', null=True, blank=True) 