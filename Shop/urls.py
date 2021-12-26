from django.urls import path

from . import views

urlpatterns = [
    path('products/<int:id>', views.cats, name='index'),
    path('product/<int:id>', views.page_product, name='page_product'),
    path('', views.page_categories, name='page_categories'),
]