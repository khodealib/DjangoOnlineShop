from django.urls import path

from home import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('products/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('categories/<slug:category_slug>/', views.HomeView.as_view(), name='category_filter'),
    path('bucket/', views.BucketHomeView.as_view(), name='bucket_get_objects'),
    path('bucket/<str:key>/delete/', views.DeleteBucketObjectView.as_view(), name='bucket_delete_object'),
    path('bucket/<str:key>/download/', views.DownloadBucketObjectView.as_view(), name='bucket_download_object')
]
