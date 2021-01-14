from django.shortcuts import render
from .models import Products,Order
from django.core.paginator import Paginator



# Create your views here.

def index(request):

    productObjects = Products.objects.all()

    # Search functionality

    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        productObjects = productObjects.filter(name__icontains=item_name)

    # Pagination

    paginator = Paginator(productObjects, 4)
    page = request.GET.get('page')
    productObjects = paginator.get_page(page)
    
    return render(request,'shop/index.html',{'productObjects':productObjects})


def detail(request, id):

    productObject = Products.objects.get(id=id)
    return render(request,'shop/detail.html',{'productObject':productObject})



def checkout(request):

    if request.method == 'POST':
        items = request.POST.get('items', "")
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        address = request.POST.get('address', "")
        city = request.POST.get('city', "")
        state = request.POST.get('state', "")
        zipCode = request.POST.get('zipCode', "")
        total = request.POST.get('total', "")

        order = Order(items=items, name=name, email=email, address=address, city=city, state=state, zipCode=zipCode, total=total)
        order.save()

    return render(request,'shop/checkout.html')