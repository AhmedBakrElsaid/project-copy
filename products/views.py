from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Product , Brand , Category

# Create your views here.



def product_list (request):
    # products = Product.objects.all()
    products = Product.objects.all()
    return render(request,'products/product_list_test.html',{'products':products})


class ProductList (ListView):
    model = Product
    paginate_by = 50



class ProductDetail (DetailView):
    model = Product




class BrandList (ListView):
    model = Brand

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class BrandDetail (DetailView):
    model = Brand

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand = self.get_object()
        context["brand_products"] = Product.objects.filter(brand = brand)
        return context
    

class CategoryList (ListView):
    model = Category