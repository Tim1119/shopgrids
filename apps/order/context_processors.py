from apps.order.models import Order,OrderItem
from apps.order.enums import OrderStatus


from apps.profiles.models import Profile
from apps.order.models import Order, OrderStatus
from django.shortcuts import get_object_or_404

def cart_context(request):
    """Inject the cart item details into all templates."""
    if request.user.is_authenticated:
        customer_profile = get_object_or_404(Profile, user=request.user)
        order, created = Order.objects.get_or_create(order_status=OrderStatus.PENDING, customer=customer_profile)
        order_items = order.orderitem_set.all()  # Use the reverse relationship
        # order_items = []
        # order = None

    else:
        order_items = []
        order = None

    return {
        "order_items": order_items,
        "order": order,
    }

