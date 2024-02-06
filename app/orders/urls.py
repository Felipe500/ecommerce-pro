from django.urls import path
from . import views

urlpatterns = [
    path('place_order/', views.place_order, name='place_order'),
    path('place_order_mercado_pago/', views.place_order_mercado_pag, name='place_order_mercado_pago'),
    path('place_order_pix/', views.place_order_mercado_pag_pix, name='place_order_mercado_pago_pix'),
    path('place_order_pagseguro/', views.place_order_pagseguro, name='place_order_pagseguro'),
    path('payments/', views.payments, name='payments'),
    path('order_complete/', views.order_complete, name='order_complete'),
]
