from django.db import models

# Create your models here.
class Contact(models.Model):
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