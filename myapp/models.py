from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    salary = models.IntegerField()
    phone = models.IntegerField()

    def __str__(self):
        return self.name
