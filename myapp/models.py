from django.db import models

class contactEnquiry(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    age = models.IntegerField()
    occupation = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.firstname
