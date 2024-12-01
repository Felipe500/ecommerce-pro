from django.urls import path
from .views import PaymentMercadoPagoAPIView, WebHookMercadoPagoAPIView, IPNMercadoPagoAPIView

urlpatterns = [
    path("process_payment/mercadopago", PaymentMercadoPagoAPIView.as_view(), name="process_payment"),
    path("webhook/mercadopago", WebHookMercadoPagoAPIView.as_view(), name="webhook"),
    path("ipn/mercadopago", IPNMercadoPagoAPIView.as_view(), name="ipn"),
]
