# Generated by Django 4.0.5 on 2022-07-01 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_app', '0003_alter_student_favorite_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='favorite_color',
            field=models.CharField(max_length=198, null=True),
        ),
    ]
