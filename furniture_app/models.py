from django.db import models

# Create your models here.
class Orders(models.Model):
    name=models.CharField(max_length=50,null=False)
    email=models.EmailField(null=False)
    mobile=models.BigIntegerField(null=False)
    service=models.CharField(max_length=50,null=False)
    # budget=models.CharField(max_length=20,null=False)
    note=models.CharField(max_length=20,null=False)


class Contact(models.Model):
    Name=models.CharField(max_length=50,null=False)
    Email=models.EmailField(null=False)
    Subject=models.CharField(max_length=50,null=False)
    Message=models.CharField(max_length=300,null=False)



