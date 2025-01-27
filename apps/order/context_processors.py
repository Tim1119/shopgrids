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


from apps.order.models import Order, OrderItem
from apps.order.enums import OrderStatus
from apps.profiles.models import Profile
from django.shortcuts import get_object_or_404

def cart_context(request):
    """
    Context processor to inject cart information into all templates.
    Also handles product-specific order item quantities for detail pages.
    """
    if request.user.is_authenticated:
        customer_profile = get_object_or_404(Profile, user=request.user)
        order, created = Order.objects.get_or_create(
            order_status=OrderStatus.PENDING, 
            customer=customer_profile
        )
        order_items = order.orderitem_set.all()
        
        # Get product_id from URL if we're on a product detail page
        try:
            # This assumes your product detail URL pattern includes 'product_id'
            if 'product_id' in request.resolver_match.kwargs:
                product_id = request.resolver_match.kwargs['product_id']
                # Get the specific order item for this product
                current_order_item = order_items.filter(product_id=product_id).first()
            else:
                current_order_item = None
        except (AttributeError, TypeError):
            # Handle cases where resolver_match isn't available
            current_order_item = None
            
    else:
        order_items = []
        order = None
        current_order_item = None

    return {
        "order_items": order_items,
        "order": order,
        "order_item": current_order_item,  # This will be available in all templates
    }