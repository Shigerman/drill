# Generated by Django 3.1.6 on 2021-03-19 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210308_1802'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testsummary',
            old_name='is_user_answer_correct',
            new_name='is_correct',
        ),
    ]