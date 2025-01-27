from apps.order.views import cart
from .views import cart_item_update,add_to_cart,cart_item_delete,cart_item_update
from django.urls import path

app_name='order'

urlpatterns = [
    path('cart/',cart,name='cart'),
     path('cart/item/update/<uuid:item_id>/', cart_item_update, name='cart_item_update'),
    path('cart/item/delete/<uuid:item_id>/', cart_item_delete, name='cart_item_delete'),
    # path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('add-to-cart/<uuid:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart-item-update/<uuid:product_id>/', cart_item_update, name='cart_item_update'),
]
