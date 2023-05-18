from django.db import models

# Create your models here.

GENDER_OPTIONS = (('male','Male'),('female','Female'))

class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    gender = models.CharField(max_length=20,choices=GENDER_OPTIONS,null=True)
    city = models.CharField(max_length=20)


    class Meta:
        db_table = 'customers'