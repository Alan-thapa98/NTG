# Generated by Django 3.2.6 on 2022-07-12 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question_answer', '0003_which_subject_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='which_subject',
            old_name='avatar',
            new_name='image',
        ),
    ]
