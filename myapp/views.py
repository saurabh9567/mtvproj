from django.shortcuts import render, HttpResponse
from .models import Product
# Create your views here.
def index(request):

    prod = Product.objects.order_by('name')
    dic = {'prod': prod}
    return render(request, 'myapp/index.html', dic)


def index1(request):
    return HttpResponse('hiiiii')
