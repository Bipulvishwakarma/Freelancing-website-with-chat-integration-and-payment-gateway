from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, Edituserprofile
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import Customer
from django.http import HttpResponse
from .models import *
from django.core.files.storage import FileSystemStorage
from .models import Product
from .forms import ProductForm
from .forms import OrderForm
from .models import OrderItem
from .forms import OrderItemForm
from django.http import JsonResponse
import json
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
# Create your views here.

# signup


def sign_up(request):
    form_class = SignUpForm
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            customer = User.customer
            # customer.save()
    else:
        fm = SignUpForm()

    return render(request, 'enroll/signup.html', {'form': fm})


# login
def user_login(request):
    # if not request.user.is_authenticated:
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)

                return HttpResponseRedirect('/home/', {'name': request.user})
                # return render(request,'enroll/index.html',{'name':request.user,'form':fm})
                # return render(request,'home.html',{'name':request.user})
    else:
        fm = AuthenticationForm()

    return render(request, 'enroll/userlogin.html', {'form': fm})


# profile

def user_profile(request):
    form_class = Edituserprofile
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = Edituserprofile(request.POST, instance=request.user)
            if fm.is_valid():
                fm.save()
        else:

            fm = Edituserprofile(instance=request.user)
        return render(request, 'enroll/profile.html', {'name': request.user, 'form': fm})
    else:
        return HttpResponseRedirect('/')

# logout


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def home(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    prices = Product.objects.all()
    context = {'products': products, 'prices': prices, 'cartItems': cartItems}

    return render(request, 'enroll/home.html', context)


def home2(request):
    return render(request, 'enroll/home2.html')


def dashboard(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    context = {'orders': orders, 'customers': customers}
    return render(request, 'enroll/dashboard.html', context)

def gendashboard(request):
    return render(request,'enroll/gen_dashboard.html')

def seller(request):
    context = {}
    return render(request, 'enroll/seller.html')


def podcast(request):

    return render(request, 'enroll/podcast.html')


def product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    form = ProductForm()
    return render(request, 'enroll/product_register.html', {'form': form})


def details(request, pk):
    prod = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'enroll/product_details.html', context)


def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()

    form = OrderForm()
    return render(request, 'enroll/order.html', {'form': form})


def orderitem(request):
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            form.save()

    form = OrderItemForm()
    return render(request, 'enroll/item.html', {'form': form})


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'enroll/cart.html', context)


def checkout(request):
    '''
    email=EmailMessage(
        'Thank you for placing order of',
        'Hiii',
    settings.EMAIL_HOST_USER,
    [request.user.email],
    )
    email.fail_silently=False
    email.send()'''
    
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.POST.get('name') and request.POST.get('description'):
                Post=Delivery()
                Post.name=request.user
                #Post.name= request.POST.get('name')
                Post.description= request.POST.get('description')
                #Post.country= request.POST.get('country')
                print("successfully saved in DB")
                Post.save()
        
                email=EmailMessage(
                    'Thank you for placing order!!',
                    'Stay in Connection with seller for Good work.',
            settings.EMAIL_HOST_USER,
            [request.user.email],
            )
            email.fail_silently=False
            email.send()
                #return render(request,'enroll/checkout.html',{'name':request.user})
        #return render(request, 'enroll/checkout.html') 
            
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        order={'get_cart_total':0,'get_cart_items':0}
        cartItems=order['get_cart_items']
        items=[]
    context={'items':items,'order':order,'cartItems':cartItems}        
    return render(request,'enroll/checkout.html',context)
    #return render(request,'enroll/checkout.html',{'name':request.user})

def contact(request):
    if request.method == "POST":
        #email = request.POST['email']
        email = "vishwahome23@gmail.com"
        message = request.POST['message']
        send_mail(
            'Customer Query',
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
    return render(request, 'contact.html')

# search

def search(request):
    query = request.GET['query']
    # allprod=Product.objects.all()
    products = Product.objects.filter(name__icontains=query)
    context = {'products': products}
    return render(request, 'enroll/search.html', context)

# updateitem

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('productId:', productId)
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)


# register custommer
def customer(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('email'):
            post = Customer()
            post.name = request.POST.get('name')
            post.email = request.POST.get('email')
            print("successfully saved in DB")
            post.save()

            return render(request, 'enroll/customer.html')

    else:
        return render(request, 'enroll/customer.html')


# Chat system using Dajngo channels

def message(request):
    return render(request, 'enroll/index.html')


def room(request, room_name):
    return render(request, 'enroll/room.html', {
        'room_name': room_name,
        #'username':username,
    })
