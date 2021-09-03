"""gs69 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from enroll import views
from django.conf.urls.static import static 
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.sign_up,name='signup'),
    path('',views.user_login,name='login'),
    path('profile/',views.user_profile,name='profile'),
    path('logout/',views.user_logout,name='logout'),
    path('home/',views.home,name='home'),
    path('home2/',views.home2,name='home2'),
    path('seller/',views.seller,name='seller'),
    path('podcast/',views.podcast,name='podcast'),
    path('cart/',views.cart,name='cart'),
    path('customer/',views.customer,name='customer'),
    path('product/',views.product,name='product'),
    path('details/<int:pk>/',views.details,name='details'),
    path('order/',views.order,name='order'),
    path('checkout/',views.checkout,name='checkout'),
    path('contact/',views.contact,name='contact'),
    path('orderitem/',views.orderitem,name='orderitem'),
    path('search/',views.search,name='search'),
    path('updateItem/',views.updateItem,name='updateItem'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('gendashboard/',views.gendashboard,name='gendashboard'),

    path('oauth/',include('social_django.urls', namespace='social')),
    path('message/',views.message,name='message'),
    path('<str:room_name>/', views.room, name='room'),
]

urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)