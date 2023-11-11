from django.urls import path

from home import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('products/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('bucket/', views.BucketHomeView.as_view(), name='bucket')
]
