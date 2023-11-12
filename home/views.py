from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from home import tasks
from home.models import Product


class HomeView(View):

    def get(self, request):
        products = Product.objects.filter(available=True)
        return render(request, 'home/index.html', {'products': products})


class ProductDetailView(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        return render(request, 'home/product_detail.html', {'product': product})


class BucketHomeView(LoginRequiredMixin, View):
    def get(self, request):
        objects = tasks.all_bucket_objects_task()
        return render(request, 'home/bucket.html', {'objects': objects})


class DeleteBucketObjectView(View):
    def get(self, request, key):
        tasks.delete_object_task.delay(key)
        messages.success(request, 'your object will delete soon.', 'info')
        return redirect('home:bucket_get_objects')
