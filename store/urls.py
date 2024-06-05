from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('masks/', views.mask_list, name='mask_list'),
    path('caps/', views.cap_list, name='cap_list'),
    path('product/<int:product_id>/<str:product_type>/', views.product_detail, name='product_detail'),
    path('custom-order/', views.custom_order, name='custom_order'),
    path('add-mask/', views.add_mask, name='add_mask'),
    path('add-surgical-cap/', views.add_surgical_cap, name='add_surgical_cap'),
    path('add-custom-order/', views.add_custom_order, name='add_custom_order'),
    path('search/', views.search_products, name='search_products'),

]
