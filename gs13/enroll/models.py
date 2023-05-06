from django.db import models

class Student(models.Model):
    stuid=models.IntegerField()
    stuname=models.CharField(max_length=70)
    stuemail=models.EmailField(max_length=70)
    stupass=models.CharField(max_length=70)

    # def __str__(self): #__str__ method is used to display an object in Django admin site
    #     return str(self.stuid)
 