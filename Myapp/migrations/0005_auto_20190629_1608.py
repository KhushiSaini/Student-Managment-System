# Generated by Django 2.2.2 on 2019-06-29 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0004_student_attendance'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='eligibility',
            field=models.CharField(default='yes', max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='marks',
            field=models.IntegerField(default=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='result',
            field=models.CharField(default='pass', max_length=30),
            preserve_default=False,
        ),
    ]
