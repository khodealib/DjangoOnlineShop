from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from home.models import Product
from orders import payments
from orders.cart import Cart
from orders.forms import CartAddForm
from orders.models import Order, OrderItem


class CartView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'orders/cart.html', {'cart': cart})


class CartAddView(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddForm(request.POST)
        if form.is_valid():
            cart.add(product, form.cleaned_data['quantity'])
            messages.success(request, f'Add {product.name} to cart successfully.', 'info')
        return redirect('orders:cart')


class CartRemoveView(View):
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        messages.success(request, f'{product.name} remove from cart.', 'info')
        return redirect('orders:cart')


class OrderCreateView(LoginRequiredMixin, View):
    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user)
        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'], price=item['price'],
                                     quantity=item['quantity'])
        cart.clear()
        return redirect('orders:order_detail', order.id)


class OrderDetailView(LoginRequiredMixin, View):
    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        return render(request, 'orders/order_detail.html', {'order': order})


class OrderPayView(LoginRequiredMixin, View):
    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        request.session['order_pay'] = {
            'order_id': order.id
        }
        pay_link = payments.send_request(request, order.get_total_price)
        return redirect(pay_link)


class OrderPayVerifyView(LoginRequiredMixin, View):
    def get(self, request):
        order_id = request.session['order_pay'].get('order_id')
        order = get_object_or_404(Order, id=order_id)
        is_pay, ref_id = payments.verify(request.GET.get('Authority'), order.get_total_price)
        if is_pay:
            order.paid = True
            order.save()
            messages.success(request, f'Transaction is successfully, Ref ID: {ref_id}', 'success')
            return render(request, 'orders/payment_result.html')
        messages.error(request, 'Transaction is failed or canceled', 'danger')
        return render(request, 'orders/payment_result.html')
