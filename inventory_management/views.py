from http.client import HTTPResponse
from django.shortcuts import render,HttpResponse

from inventory_management.forms import coupon, inventory_form
from inventory_management.models import Product

# to post all products
def inventory_look(request):
    context = {}
    context['inventory_form'] = inventory_form

    if request.method == 'POST':
        obj_inventory = Product()
        obj_inventory.name = request.POST['name']
        obj_inventory.sku = request.POST['sku']
        obj_inventory.price = request.POST['price']
        obj_inventory.quantity_in_stock = request.POST['quantity_in_stock']
        obj_inventory.save()
        return HttpResponse("Data Saved Succesfully!")

    return render(request,'inventoryproducts.html',context)

# to get all products

def inventory_get(request):
    context = {}
   

    obj_get = Product.objects.all()
    context['obj_get'] = obj_get
    return render(request,'inventory_getallproducts.html',context)


# to update specific products
def inventory_update(request,id):
    obj_update = Product.objects.get(pk=id)
    context = {}
    context['inventory_form'] = inventory_form(instance=obj_update)

    if request.method == 'POST':
        obj_update.name = request.POST['name']
        obj_update.sku = request.POST['sku']
        obj_update.price = request.POST['price']
        obj_update.quantity_in_stock = request.POST['quantity_in_stock']
        obj_update.save()
        return HttpResponse("Data Saved Succesfully!")

    return render(request,'inventoryproductsupdate.html',context)


#################CART MANAGEMENT################################

# def addproduct_tocart(request):
#     context = {}
#     context['addproduct'] = addproduct

#     if request.method == 'POST':
#         obj_addproduct = Product()
#         obj_addproduct.name = request.POST['name']
#         obj_addproduct.sku = request.POST['sku']
#         obj_addproduct.price = request.POST['price']
#         obj_addproduct.quantity_in_stock = request.POST['quantity_in_stock']
#         obj_addproduct.save()
#         return HttpResponse("Data Saved Succesfully!")

#     return render(request,'inventoryproductsupdate.html',context)


#################COUPON MANAGEMENT################################

def coupon_management(request):
    context = {}
    context['coupon'] = coupon

    if request.method == 'POST':
        obj_coupon = coupon
        obj_coupon.code = request.POST['code']
        obj_coupon.valid_from = request.POST['valid_from']
        obj_coupon.valid_to = request.POST['valid_to']
        obj_coupon.discount = request.POST['discount']
        obj_coupon.active = request.POST['active']
        obj_coupon.sku = request.POST['sku']
        obj_coupon.quantity_in_stock = request.POST['quantity_in_stock']
        obj_coupon.save()
    
        if obj_coupon.active:
            return HttpResponse(obj_coupon.discount)
        else:
            return HttpResponse('Sorry Coupon Expired')
    return render(request,'couponsinfo.html',context)
    


