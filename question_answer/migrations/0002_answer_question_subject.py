# Generated by Django 3.2.6 on 2022-07-12 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_answer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer_question',
            name='subject',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
