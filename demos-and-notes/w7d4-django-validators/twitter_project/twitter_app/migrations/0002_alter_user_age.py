# Generated by Django 4.0.6 on 2022-07-07 15:55

from django.db import migrations, models
import twitter_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(validators=[twitter_app.models.validate_age]),
        ),
    ]
