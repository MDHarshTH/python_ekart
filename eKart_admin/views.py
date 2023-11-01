from random import randint
from django.conf import settings
from django.shortcuts import redirect, render
from django.core.mail import send_mail

from customer.models import Seller
from eKart_admin.models import Category

# Create your views here.
def admin_home(request):
    return render(request,'ekart_admin/admin_home.html')

def view_category(request):
    return render(request,'ekart_admin/view_category.html')

def add_category(request):
    message = ''
    if request.method == 'POST':
        category_name = request.POST['category_name']
        discrip = request.POST['description']
        category_image = request.FILES['category_image']
        
        category_exist = Category.objects.filter(category_name = category_name).exists()
        if not category_exist:
            category = Category (
                category_name = category_name,
                discription = discrip,
                cover_picture = category_image
            )

            category.save()
            message = 'Created'
        else:
            message = "Category Already Exist"

    return render(request,'ekart_admin/add_category.html',{'message':message})

def approve_seller(request, id):
    seller = Seller.objects.get(id = id)
    seller_id = randint(111111,999999)
    temporary_password = 'sel-' + str(seller_id)
    subject = 'Login credentials'
    message = 'Hai! Your Ekart Account Has Been Approved. Your Id Is ' + str(seller_id) + 'And Password Is' + temporary_password
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [seller.email]
    send_mail(
        subject,
        message,
        from_email,
        recipient_list
    )
    Seller.objects.filter(id = id).update(login_id = seller_id, password = temporary_password, status = 'Approved')
    return redirect('ekart_admin:pending_sellers')

def pending_sellers(request):
    pending_list = Seller.objects.filter(status = 'pending',)
    return render(request,'ekart_admin/pending_sellers.html',{'list': pending_list})

def approved_sellers(request):
    return render(request,'ekart_admin/approved_sellers.html')

def customers(request):
    return render(request,'ekart_admin/customers.html')

def admin_login(request):
    return render(request,'ekart_admin/admin_login.html')

