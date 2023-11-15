from django.shortcuts import get_object_or_404, redirect, render
from random import randint
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import F

from customer.models import Cart, Customer
from seller.models import Product, Seller
# from .models import Customer
# Create your views here.


def customer_home(request):
    customer = Customer.objects.get(id = request.session['customer'])
    products = Product.objects.all()
    context = {
        'products':products,
        'customer_details':customer
    }
    return render(request, 'customer/customer_home.html',context)


def store(request):
    query = request.GET.get('query')
    if query == 'all':
        product = Product.objects.all()
    else:
        product = Product.objects.filter(product_category = query)
    return render(request, 'customer/store.html',{'product':product})


def product_detail(request, id):
    message = ''
    product = Product.objects.get(id = id)
    customer = Customer.objects.get(id = request.session['customer'])
    # product_exist = Cart.objects.filter(product_id = id).exists()
    if request.method == 'POST':
        if 'customer' in request.session:
            cart = Cart(
                customer = customer,
                product = product,
                price = product.price
            )
            cart.save()
            message = "Added to cart"

        else:
            message = "Not added to cart"
            return redirect('customer:login')
        
    try:
        cart_item = get_object_or_404(Cart, customer = customer, product_id = id)
        item_exist = True
    except Exception as e:
        item_exist = False
    
    context = {
        'product':product,
        'message':message,
        'item_exist':item_exist
    }



    return render(request, 'customer/product_detail.html',context)


def cart(request):
    customer = Customer.objects.get(id = request.session['customer'])
    cart = Cart.objects.filter(customer_id = customer.id).annotate(sub_total = F('quantity') * F('price'))
    grand_total = 0
    for item in cart:
        grand_total += item.sub_total

    context = {
        'cart':cart,
        'customer_details':customer, 
        'grand_total':grand_total
    }
    return render(request, 'customer/cart.html',context)

def  cart_remove(request, id):
    item = Cart.objects.get(id = id)
    item.delete()
    return redirect('customer:cart')


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