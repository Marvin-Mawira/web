from django.urls import path
# from . import views
from ecommerce import views
import ecommerce  # Import the 'ecommerce' module
from .views import buy_product



urlpatterns = [
    path('', views.index, name='index' ),
    path('fruit/', views.fruit, name='fruit' ),
    path('service/', views.service, name='service' ),
    path('contact/', views.contact, name='contact' ),
    path('success/', views.success, name='success' ),
    path('login/', views.login, name='login' ),
    
    # path('product_detail/', views.product_detail, name='product_detail' ),
    path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
]