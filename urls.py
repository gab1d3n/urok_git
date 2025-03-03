from django.urls import path
from .views import product_view, success_page

urlpatterns = [
    path('products/', product_view, name='product_form'),
    path('success/', success_page, name='success_page'),
]
