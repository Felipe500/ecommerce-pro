from rest_framework.permissions import AllowAny
from rest_framework.views import APIView, View
from rest_framework.response import Response

from django.shortcuts import redirect, render

import mercadopago


sdk = mercadopago.SDK("APP_USR-8646436938896420-122216-aa13a9a165cfa89baa451e2a4f498912-231157397")


class PaymentMercadoPagoAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        print('post ', self.request.POST)
        print('self.request.data ', self.request.data)
        request_data = request.data

        request_options = mercadopago.config.RequestOptions()
        request_options.custom_headers = {
            'x-idempotency-key': '<SOME_UNIQUE_VALUE>'
        }
        id_order_payment = request_data.pop('id_order_payment')
        payment_response = sdk.payment().create(request_data)
        payment_response_status = payment_response["status"]

        payment = payment_response["response"]

        if payment_response_status in [200, 201]:
            print("status =>", payment["status"])
            print("status_detail =>", payment["status_detail"])
            print("id=>", payment["id"])
            print(id_order_payment)
            print(payment)
            if payment["payment_method_id"] == "pix":
                return render('orders/payments_qrcode_pix.html', {'payment': payment})

            return Response({'message': 'in_progress', 'status_detail': payment["status_detail"]})
        else:
            print(payment["status"])
            print(payment)
            return Response(payment)


class WebHookMercadoPagoAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        print('WebHook ', self.request.data)
        return Response(request.data)


class IPNMercadoPagoAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        print('IPN ', self.request.data)
        return Response(request.data)
