import json

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView, View
from rest_framework.response import Response
from django.shortcuts import reverse

import mercadopago

from app.carts.models import CartItem
from app.orders.models import Order, Payment, OrderProduct, Product

sdk = mercadopago.SDK("APP_USR-8646436938896420-122216-aa13a9a165cfa89baa451e2a4f498912-231157397")


class PaymentMercadoPagoAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        request_data = request.data
        order_number = request_data.pop('order_number')
        request_data['external_reference'] = order_number
        request_data['notification_url'] = "https://f16f-177-12-134-168.ngrok-free.app/" + reverse('webhook')

        request_options = mercadopago.config.RequestOptions()
        request_options.custom_headers = {
            'x-idempotency-key': order_number
        }

        payment_response = sdk.payment().create(request_data)

        payment_data = payment_response["response"]
        print(payment_data)

        if payment_response["status"] in [200, 201]:
            print("status =>", payment_data["status"])
            print("status_detail =>", payment_data["status_detail"])
            print("id=>", payment_data["id"])
            print(order_number)
            print(payment_data)

            order = Order.objects.get(user=request.user, is_ordered=False, order_number=order_number)

            payment = Payment(
                user=request.user,
                payment_id=payment_data['id'],
                payment_method=payment_data['payment_method_id'],
                payment_method_id=payment_data['payment_method_id'],
                payment_type_id=payment_data['payment_type_id'],
                amount_paid=order.order_total,
                status=payment_data['status'],
                date_of_expiration=payment_data['date_of_expiration'],
                transaction_data=payment_data['point_of_interaction']['transaction_data']
            )

            payment.save()

            order.payment = payment

            # Move the cart items to Order Product table
            cart_items = CartItem.objects.filter(user=request.user)

            for item in cart_items:
                orderproduct = OrderProduct()
                orderproduct.order_id = order.id
                orderproduct.payment = payment
                orderproduct.user_id = request.user.id
                orderproduct.product_id = item.product_id
                orderproduct.quantity = item.quantity
                orderproduct.product_price = item.product.price
                orderproduct.ordered = True
                orderproduct.save()

                cart_item = CartItem.objects.get(id=item.id)
                product_variation = cart_item.variations.all()
                orderproduct = OrderProduct.objects.get(id=orderproduct.id)
                orderproduct.variations.set(product_variation)
                orderproduct.save()

                # Reduce the quantity of the sold products
                product = Product.objects.get(id=item.product_id)
                product.stock -= item.quantity
                product.save()

            # Clear cart
            CartItem.objects.filter(user=request.user).delete()

            url_redirect = request.build_absolute_uri('/')[:-1] + reverse('wait_for_payment', args=[order.id])

            if payment_data['status'] == "pending":
                order.status = 'await_payment'
                url_redirect = request.build_absolute_uri('/')[:-1] + reverse('wait_for_payment', args=[order.id])
            elif payment_data['status'] == "approved":
                order.is_ordered = True
                order.status = 'waiting_for_shipping'
                url_redirect = request.build_absolute_uri('/')[:-1] + reverse('order_complete')
            else:
                order.status = 'payment_error'

            order.save()
            return Response({'status': payment_data["status"],
                             'data': payment_data,
                             'url_redirect': url_redirect})
        else:
            print(payment_data["status"])
            print(payment_data)
            return Response(payment_data)


class WebHookMercadoPagoAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        print('WebHook ', self.request.data)
        print(self.request.data)
        data = self.request.data
        if data.get('action', None) == "payment.updated":
            get_payment_response = sdk.payment().get(data['data']['id'])
            print(get_payment_response)

        return Response(request.data)


class IPNMercadoPagoAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        print('IPN ', self.request.data)
        print(self.request.query_params)
        return Response(request.data)
