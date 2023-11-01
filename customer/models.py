from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email= models.CharField(max_length = 50)
    gender = models.CharField(max_length = 20)
    city = models.CharField(max_length = 30)
    country = models.CharField(max_length = 30)
    password = models.CharField(max_length = 20)

    class Meta:
        db_table = 'customer_tb'


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

