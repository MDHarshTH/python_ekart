from django.shortcuts import redirect, render
from random import randint
from django.conf import settings
from django.core.mail import send_mail

from customer.models import Customer, Seller
# from .models import Customer
# Create your views here.


def customer_home(request):
    customer = Customer.objects.get(id = request.session['customer'])
    return render(request, 'customer/customer_home.html',{'customer_details':customer})


def store(request):
    return render(request, 'customer/store.html')


def product_detail(request):
    return render(request, 'customer/product_detail.html')


def cart(request):
    return render(request, 'customer/cart.html')


def place_order(request):
    return render(request, 'customer/place_order.html')


def order_complete(request):
    return render(request, 'customer/order_complete.html')


def dashboard(request):
    return render(request, 'customer/dashboard.html')


def seller_register(request):
    status = False
    msg = ''
    if request.method == 'POST':
        f_name = request.POST['fname']
        l_name = request.POST['lname']
        email = request.POST['email']
        gender = request.POST['gender']
        city = request.POST['city']
        country = request.POST['country']
        cmp_name = request.POST['cmpname']
        bank_name = request.POST['bname']
        bank_branch = request.POST['bbranch']
        accno = request.POST['accnum']
        ifsc = request.POST['ifsccode']
        seller_image = request.FILES['uploadimage']

        seller_exist = Seller.objects.filter(email = email).exists()
        if not seller_exist : 
            seller = Seller ( 
                first_name = f_name,
                last_name = l_name,
                email = email,
                gender = gender,
                city = city,
                country = country,
                company_name = cmp_name,
                seller_picture = seller_image,
                account_number = accno,
                ifsc = ifsc,
                bank_name = bank_name, 
                bank_branch =  bank_branch
            )

            seller.save()
            msg = 'ACCOUNT CREATED SUCCESSFULLY'
            status = True
        else :
            msg = 'EMAIL ALREADY EXIST'

    return render(request, 'customer/seller_register.html',{'message' : msg})


def seller_login(request):

    msg = ''
    if request.method == 'POST':
        S_Id = request.POST['sellerid']
        S_password = request.POST['sellerpass']

        newSeller = Seller.objects.filter(login_id = S_Id,password = S_password)

        if newSeller.exists():
            request.session['seller'] = newSeller[0].id
            request.session['seller_name'] = newSeller[0].first_name + ' ' + newSeller[0].last_name
            return redirect('Seller:seller_home')
        # msg = 'SUCCESSFULLY LOGIN'
        else:
            msg = 'Incorrect Password or Username'
            

    return render(request, 'customer/seller_login.html',{'message':msg})

def customer_signup(request):

    status = False
    msg = ""

    if request.method == 'POST':
        f_name = request.POST['fname']
        l_name = request.POST['lastname']
        email = request.POST['email']
        gender = request.POST['gender']
        city = request.POST['city']
        country = request.POST['country']
        password = request.POST['password']

        customer_exist = Customer.objects.filter(email = email).exists()
        
        if not customer_exist: 
            customer = Customer(
            first_name = f_name,
            last_name = l_name,
            email = email,
            gender = gender,
            city = city,
            country = country,
            password = password
            )
            customer.save()
            msg = 'REGISTERED SUCCESSFULL'
            status = True
        else:
            msg = 'ALREADY REGISTERED'
    return render(request, 'customer/customer_signup.html', {'message': msg,'status':status})


def customer_login(request):
    msg = ''
    if request.method == 'POST':
        c_email = request.POST['email']
        c_password = request.POST['password']

        customer = Customer.objects.filter(email = c_email,password = c_password)

        if customer.exists():
            request.session['customer'] = customer[0].id
            return redirect('customer:customer_home')
        # msg = 'SUCCESSFULLY LOGIN'
    else:
        msg = 'Incorrect Password or Username'
    return render(request, 'customer/customer_login.html',{'message':msg})




def forgot_password_customer(request):
    return render(request, 'customer/forgot_password_customer.html')


def forgot_password_seller(request):
    return render(request, 'customer/forgot_password_seller.html')