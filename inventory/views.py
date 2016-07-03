from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from .models import Item, Vendor
from django.contrib.auth import logout
from django.db.models import F
from django.core.mail import EmailMessage
from django.contrib import messages


def index(request):
    try:
        return render(request, 'inventory/index.html', {'context': get_list_or_404(Item)})
    except Exception as e:
        return render(request, 'inventory/index.html', {'e': e})


def scan(request):
    return render(request, 'inventory/scan.html')


def vendors(request):
    try:
        return render(request, 'inventory/vendors.html', {'context': get_list_or_404(Vendor)})
    except Exception as e:
        return render(request, 'inventory/vendors.html', {'error': e})


def listing(request, vendor=None):
    context = []
    try:
        if vendor:
            search = get_list_or_404(Item, item_vendor=Vendor.objects.filter(vendor_name=vendor))
        else:
            search = get_list_or_404(Item)

        for item in search:
            product = {}
            if item.item_quantity <= item.item_order_point:
                quantity = item.item_max_quantity - item.item_quantity
                product['name'] = item.item_name
                product['quantity'] = quantity
                context.append(product)
        return render(request, 'inventory/list.html', {'context': context, 'vendor': vendor})

    except Exception as e:
        print(e)
        message = "{0} has no items".format(vendor)
        if not vendor:
            message = "There are no needed items"
        return render(request, 'inventory/logout.html', {'message': message})


def remove(request):
    if request.method == 'GET':
        return render(request, 'inventory/remove.html')
    elif request.method == 'POST':
        try:
            barcode = request.POST.get('barcode')
            quantity = request.POST.get('quantity')
            item = Item.objects.get(item_barcode=barcode)
            Item.objects.filter(item_barcode=barcode).update(item_quantity=F('item_quantity') - quantity)
            return render(request, 'inventory/remove.html', {'message': "Successfully removed {0} {1}"
                                                                        "".format(quantity, item.item_name)})
        except Exception as e:
            print(e)
            return render(request, 'inventory/remove.html', {'error': "Item does not exist in inventory"})


def add(request):
    if request.method == 'GET':
        return render(request, 'inventory/add.html')
    elif request.method == 'POST':
        try:
            barcode = request.POST.get('barcode')
            quantity = request.POST.get('quantity')
            item = Item.objects.get(item_barcode=barcode)
            Item.objects.filter(item_barcode=barcode).update(item_quantity=F('item_quantity') + quantity)
            return render(request, 'inventory/add.html', {'message': "Successfully added {0} {1}"
                                                                     "".format(quantity, item.item_name)})
        except Exception as e:
            print(e)
            return render(request, 'inventory/add.html', {'error': "Item does not exist in inventory"})


def help_page(request):
    return render(request, 'inventory/help.html')


def send_mail(request, vendor=None):
    try:
        order_list = []
        if vendor:
            context = get_list_or_404(Item, item_vendor=Vendor.objects.filter(vendor_name=vendor))

        else:
            context = get_list_or_404(Item)
        address = get_object_or_404(Vendor, vendor_name=vendor).vendor_email
        for i in context:
            if i.item_quantity <= i.item_order_point:
                order_list.append(i.item_name + " " + str(i.item_max_quantity - i.item_quantity) + "\n")
        s = "".join(order_list)
        try:
            email = EmailMessage(subject="Order for {0}".format(vendor),
                                 body=s,
                                 to=[address])
            email.send()
            messages.add_message(request, messages.INFO, "Email was sent to {}".format(vendor))
            return redirect('inventory:index')
        except Exception as e:
            return render(request, 'inventory/logout.html', {'message': e})

    except Exception as e:
        return render(request, 'inventory/logout.html', {'message': e})


def logout_function(request):
    logout(request)
    return render(request, 'inventory/logout.html', {'message': "Bye Felicia"})
