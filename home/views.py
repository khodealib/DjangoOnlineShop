from django.shortcuts import render, get_object_or_404
from django.views import View

from home.models import Product
from home.tasks import all_bucket_objects_task


class HomeView(View):

    def get(self, request):
        products = Product.objects.filter(available=True)
        return render(request, 'home/index.html', {'products': products})


class ProductDetailView(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        return render(request, 'home/product_detail.html', {'product': product})


class BucketHomeView(View):
    def get(self, request):
        objects = all_bucket_objects_task()
        return render(request, 'home/bucket.html', {'objects': objects})
