from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from home import tasks
from home.models import Product, Category
from utils.mixins import IsAdminUserMixin


class HomeView(View):

    def get(self, request, category_slug=None):
        products = Product.objects.filter(available=True)
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)
        categories = Category.objects.all()
        return render(request, 'home/index.html', {'products': products, 'categories': categories})


class ProductDetailView(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        return render(request, 'home/product_detail.html', {'product': product})


class BucketHomeView(IsAdminUserMixin, View):
    def get(self, request):
        objects = tasks.all_bucket_objects_task()
        return render(request, 'home/bucket.html', {'objects': objects})


class DeleteBucketObjectView(IsAdminUserMixin, View):
    def get(self, request, key):
        tasks.delete_object_task.delay(key)
        messages.success(request, 'your object will delete soon.', 'info')
        return redirect('home:bucket_get_objects')


class DownloadBucketObjectView(IsAdminUserMixin, View):
    def get(self, request, key):
        tasks.download_object_task.delay(key)
        messages.success(request, 'your download will start soon', 'success')
        return redirect('home:bucket_get_objects')
