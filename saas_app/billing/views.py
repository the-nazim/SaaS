from django.shortcuts import render
import stripe 
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.permissions import AllowAny
from rest_framework.authentication import BasicAuthentication

stripe.api_key = settings.STRIPE_SECRET_KEY

@method_decorator(csrf_exempt, name='dispatch')
class CreateCheckoutSessionView(APIView):

    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            amount = request.data.get('amount')  # Default to $10.00 if not provided
            product_name = request.data.get('product_name')
            session = stripe.checkout.Session.create(
                payment_method_types = ['card'],
                line_items = [{
                    'price_data' : {
                        'currency' : 'usd',
                        'product_data' : {
                            'name' : product_name,
                        },
                        'unit_amount' : amount,
                    },
                    'quantity' : 1,
                }],
                mode = 'payment',
                success_url = 'http://localhost:8000/success/',
                cancel_url = 'http://localhost:8000/cancel/',
            )
            return Response({'checkout': session.url}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
