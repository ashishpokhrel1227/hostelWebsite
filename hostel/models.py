from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from datetime import datetime, timedelta
import pytz

class Student(models.Model):
    ROOM_CHOICES = (
        ('Two bed', 'TWO'),
        ('Three bed', 'THREE')
    )
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = PhoneNumberField(null=True)
    entry_on = models.DateTimeField(editable=False, null=True)
    room = models.CharField(max_length=10, choices=ROOM_CHOICES, null=True)

    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'

    def save(self, *args, **kwargs):
        self.entry_on = datetime.now().replace(tzinfo=pytz.UTC)
        return super(Student, self).save(*args, **kwargs)