# Generated by Django 4.1.5 on 2023-01-24 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_rename_lesson_question_course_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='title',
        ),
    ]
