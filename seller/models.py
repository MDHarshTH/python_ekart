from django.db import models

from eKart_admin.models import Category

# Create your models here.

class Seller(models.Model):
    login_id = models.CharField(max_length = 50, default = '')
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    gender = models.CharField(max_length = 20)
    city = models.CharField(max_length = 30)
    country = models.CharField(max_length = 30)
    company_name = models.CharField(max_length = 30,default = ' ')
    password = models.CharField(max_length = 20)
    seller_picture = models.ImageField(upload_to = 'seller/')
    account_number = models.CharField(max_length = 50)
    ifsc = models.CharField(max_length = 50)
    status = models.CharField(max_length = 50,default = 'pending')
    bank_name = models.CharField(max_length = 50,default = ' ')
    bank_branch = models.CharField(max_length = 50,default = ' ')


    class Meta:
        db_table = 'seller_tb'

class Product(models.Model):
    product_no = models.CharField(max_length = 20)
    product_name = models.CharField(max_length = 50)
    product_category = models.ForeignKey(Category,on_delete = models.CASCADE)
    description = models.CharField(max_length = 200)
    stock = models.IntegerField()
    price = models.FloatField()
    image = models.ImageField(upload_to = 'product/')
    seller = models.ForeignKey(Seller,on_delete = models.CASCADE)
    status = models.CharField(max_length = 20,default = 'available')

    class Meta:
        db_table = 'product_tb'
