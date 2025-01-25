from django.shortcuts import get_object_or_404,render
from apps.products.models import Product
from apps.order.models import Order,OrderItem
from apps.order.enums import OrderStatus

# Create your views here.
# def add_to_cart(request,product_id):
#     customer_profile  = request.user.profile
#     if request.user.is_authenticated:
#         product = get_object_or_404(Product,id=product_id)
#         order,created = Order.objects.get_or_create(order_status=Order.OrderStatus.PENDING,user=customer_profile)
#         order_item,created = Order.objects.get_or_create(order_status=Order.OrderStatus.PENDING,user=customer_profile)
        
#         if not created:
#             .quantity += 1
#             cart_item.save()
#     else:
#         pass

def cart(request):
    customer_profile  = request.user.profile
    if request.user.is_authenticated:
        order,created = Order.objects.get_or_create(order_status=OrderStatus.PENDING,user=customer_profile)
        order_items = order.order_items.all()
    else:pass
    context = {"order_items":order_items,"order":order}
    return render(request,'order/cart.html',context)


