# Generated by Django 4.0.5 on 2022-07-01 16:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_app', '0006_administrator'),
    ]

    operations = [
        migrations.CreateModel(
            name='Correct',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]
