from apps.order.views import cart
from django.urls import path


urlpatterns = [
    path('cart/',cart,name='cart'),
]
