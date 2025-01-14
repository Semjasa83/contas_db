import uuid
from django.db import models
from rest_framework.exceptions import ValidationError


# Create your models here.
class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True, null=True)
    note = models.CharField(max_length=1000, blank=True, null=True)
    color = models.CharField(max_length=150, default='hsl(202, 70%, 85%)')
    company = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.firstname + ' ' + self.lastname


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    contact = models.ManyToManyField(Contact, related_name='notes')
    company = models.CharField(max_length=255)
    headline = models.CharField(max_length=255)
    note = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    priority = models.PositiveSmallIntegerField()
    color = models.CharField(max_length=150, default='hsl(202, 70%, 85%)')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if not (0 <= self.priority <= 4):
            raise ValidationError('Priority must be between 0 and 4.')

    def __str__(self):
        return self.headline