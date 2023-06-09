from django.db import models

# Create your models here.
#Class name == table name
class Product(models.Model): #Appname_tablename .,, todoapp_Product
    pname=models.CharField(max_length=50)
    pdesc=models.CharField(max_length=500)
    price=models.FloatField()
    cat=models.CharField(max_length=30)
    is_deleted=models.CharField(max_length=5)
