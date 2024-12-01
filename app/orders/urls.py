from django.urls import path
from . import views

urlpatterns = [
    path('place_order/', views.place_order, name='place_order'),
    path('save_order', views.SaveOrder.as_view(), name='save_order'),
    path('order_payment/<int:pk>', views.OrderPayments.as_view(), name='order_payment'),
    path('place_order_mercado_pago/', views.place_order_mercado_pag, name='place_order_mercado_pago'),
    path('place_order_mercado_pago/pix', views.place_order_mercado_pag_pix, name='place_order_mercado_pago_pix'),
    path('place_order_pagseguro/', views.place_order_pagseguro, name='place_order_pagseguro'),
    path('payments/<int:pk>', views.payments, name='payments'),
    path('wait_payment/<int:pk>', views.OrderWaitPayment.as_view(), name='wait_for_payment'),
    path('order_complete/', views.order_complete, name='order_complete'),
]
