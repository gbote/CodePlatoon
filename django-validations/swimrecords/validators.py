from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as text
from django.utils import timezone as tz

def valid_stroke(stroke):
  valid_strokes = ['front crawl', 'butterfly', 'breast', 'back', 'freestyle']
  if stroke not in valid_strokes:
    raise ValidationError(text(f"{stroke} is not a valid stroke"))

def valid_record_date(date):
    if date > tz.now():
        raise ValidationError(text("Can't set record in the future."))

def valid_record_break_date(date):
    if date < tz.now():
        raise ValidationError(text("Can't break record before record was set."))