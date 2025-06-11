from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from home.models import Contact
from django.contrib import messages



# Create your views here.
def index(request):
    # return HttpResponse("this is server page")
    return render(request,'index.html' )
def about(request):
    # return HttpResponse("this is about page")
     return render(request,'about.html')

def services(request):
    # return HttpResponse("this is services page")
    return render(request, 'services.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        flavor = request.POST.get('flavor')  # fixed key name (was 'Flavor')
        address = request.POST.get('address')  # fixed spacing
        quantity=request.POST.get('quantity')
        contact = Contact(name=name, flavor=flavor, phone=phone, address=address,quantity=quantity, date=datetime.today())
        contact.save()
        messages.success(request, 'Your order has been sent!')  # fixed typo: 'send' → 'sent'

        return render(request, 'contact.html', {'message': 'Order placed successfully!'})  # fixed typo: 'place' → 'placed'

    return render(request, 'contact.html')

def cart(request):
    return render(request, 'cart.html')

def flavor_view(request):
    # products = Product.objects.all()
    return render(request, 'flavor.html')

# views.py


# def add_to_cart(request, flavor_id):
#     cart = request.session.get('cart', {})
    
#     if str(flavor_id) in cart:
#         cart[str(flavor_id)] += 1
#     else:
#         cart[str(flavor_id)] = 1

#     request.session['cart'] = cart
#     return redirect('flavors')  # or wherever you want to redirect


