from django.db import models

NULL = "NULL"

# Create your models here.
class Person(models.Model):
    fname = models.CharField(null=False, max_length=50)
    lname = models.CharField(null=False, max_length=50)
    age = models.IntegerField(null=False, default=0)
    mail = models.CharField(null=False, max_length=50, default=NULL)

    def __str__(self) -> str:
        return self.fname + ' ' + self.lname