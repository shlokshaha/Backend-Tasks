from django.db import models

class UserDetails(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    phno=models.IntegerField()
    email=models.EmailField()
    gender=models.CharField(max_length=10)

    def __str__(self):
        return self.email
