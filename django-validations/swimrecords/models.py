from django.db import models
from .validators import *
from django.core.validators import *

class SwimRecord(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    team_name = models.CharField(max_length=255)
    relay = models.BooleanField()
    stroke = models.CharField(max_length=255, validators=[valid_stroke])
    distance = models.IntegerField(validators=[MinValueValidator(50)])
    record_date = models.DateTimeField(validators=[valid_record_date])
    record_broken_date = models.DateTimeField(validators=[valid_record_break_date])
