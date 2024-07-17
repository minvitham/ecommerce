"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path

from inventory_management.views import coupon_management, inventory_get, inventory_look, inventory_update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('allproducts_basic/', inventory_look,name='inventory-view'),
    path('allproducts_all/', inventory_get,name='inventory-all-products'),
    path('allproducts_update/<int:id>', inventory_update,name='inventory-update'),
    path('coupons_info/', coupon_management,name='coupons-info'),
]
