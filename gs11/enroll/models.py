from django.db import models

class student(models.Model):
    stuid=models.IntegerField(primary_key=True)
    stuname=models.CharField(max_length=70)
    stuemail=models.EmailField(max_length=70)
    stupass=models.CharField(max_length=70)
    comment=models.CharField(max_length=70, default='not_available')