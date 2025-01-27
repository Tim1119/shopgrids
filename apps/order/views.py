from django.shortcuts import get_object_or_404,render
from apps.products.models import Product
from apps.order.models import Order,OrderItem
from apps.order.enums import OrderStatus
from apps.profiles.models import Profile
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


def cart(request):
    customer_profile  = request.user.profile
    if request.user.is_authenticated:
        order,created = Order.objects.get_or_create(order_status=OrderStatus.PENDING,user=customer_profile)
        order_items = order.order_items.all()
    else:pass
    context = {"order_items":order_items,"order":order}
    return render(request,'order/cart.html',context)




@login_required
def add_to_cart(request, product_id):
    """Handle adding a product to the cart."""
    print('*************************')
    print('*************************')
    print('*************************')
    print('*************************')
    product = get_object_or_404(Product, id=product_id)
    profile = get_object_or_404(Profile, user=request.user)

    # Get the user's current order or create a new one
    order, created = Order.objects.get_or_create(
        customer=profile, 
        order_status='PENDING',  # Default to pending status
        is_paid=False
    )

    # Check if the product is already in the order
    order_item, created = OrderItem.objects.get_or_create(
        order=order, product=product, 
        defaults={'quantity': 1, 'unit_price': product.price}
    )

    if not created:
        # If the product already exists, just increase the quantity
        order_item.quantity += 1
        order_item.subtotal = order_item.quantity * order_item.unit_price
        order_item.save()

    # Return updated cart items via HTMX
    return render(request, 'order/shopping-item.html', {'order_items': order.orderitem_set.all(), 'order': order})


@login_required
def cart_item_update(request, product_id):
    """Handle cart item quantity update."""
    print('*************************')
    print('*************************')
    print('*************************')
    print('*************************')
    product = Product.objects.get(id=product_id)
    customer_profile = get_object_or_404(Profile,user=request.user)
    # order_item = get_object_or_404(OrderItem, id=item_id)

    order, created = Order.objects.get_or_create(
        customer=customer_profile, 
        order_status='PENDING',  # Default to pending status
        is_paid=False
    )

    # Check if the product is already in the order
    order_item, created = OrderItem.objects.get_or_create(
        order=order, product=product, 
        defaults={'quantity': 1, 'unit_price': product.price}
    )

    # if order_item.order.customer != request.user.profile:
    #     return JsonResponse({"error": "Unauthorized"}, status=403)

    if request.method == "POST":
        # Update quantity based on whether it's increment or decrement
        # if "quantity_btn" in request.POST:
        #     quantity_change = int(request.POST["quantity_btn"])
        print('--->',request.POST)

        # if order_item.quantity + quantity_change > 0:
        #     order_item.quantity += quantity_change
        #     order_item.save()

        order = None

        return render(request, 'order/shopping-item.html', {"order_items": order_item.order.orderitem_set.all(), "order": order})

@login_required
def cart_item_delete(request, item_id):
    """Handle item removal from the cart."""
    print('*************************')
    print('*************************')
    print('*************************')
    print('*************************')
    order_item = get_object_or_404(OrderItem, id=item_id)

    # Check if the user is authenticated and belongs to the order
    if order_item.order.customer != request.user.profile:
        return JsonResponse({"error": "Unauthorized"}, status=403)

    order_item.delete()
    return render(request, "cart/cart_items.html", {"order_items": order_item.order.orderitem_set.all(), "order": order_item.order})

# In views.py
from django.http import HttpResponse
from django.template.loader import render_to_string

# def cart_item_update(request, product_id):
#     print('*************************')
#     print('*************************')
#     print('*************************')
#     print('*************************')
#     product = Product.objects.get(id=product_id)
#     order, created = Order.objects.get_or_create(user=request.user, is_completed=False)
    
#     # Get or create order item
#     order_item, item_created = OrderItem.objects.get_or_create(
#         order=order, 
#         product=product
#     )
    
#     # Determine action based on request
#     action = request.GET.get('action', 'add')
#     if action == 'add':
#         order_item.quantity += 1
#     elif action == 'remove':
#         order_item.quantity = max(0, order_item.quantity - 1)
    
#     # Delete item if quantity becomes 0
#     if order_item.quantity == 0:
#         order_item.delete()
#     else:
#         order_item.save()
    
#     # Refresh order items
#     order_items = order.orderitem_set.all()
    
#     # Render cart items component
#     cart_html = render_to_string('cart_items.html', {
#         'order_items': order_items,
#         'order': order
#     })
    
#     return HttpResponse(cart_html)

# def cart_item_update(request, product_id):
#     print('*************************')
#     print('*************************')
#     action = request.GET.get('action')
#     product = get_object_or_404(Product, id=product_id)
    
#     if request.user.is_authenticated:
#         customer_profile = get_object_or_404(Profile, user=request.user)
#         order, created = Order.objects.get_or_create(order_status=OrderStatus.PENDING, customer=customer_profile)
#         order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
        
#         if action == 'add':
#             order_item.quantity += 1
#         elif action == 'remove':
#             if order_item.quantity > 1:
#                 order_item.quantity -= 1
#             else:
#                 order_item.delete()
        
#         order_item.save()
        
#         # Re-fetch the order items to get the updated list
#         order_items = order.orderitem_set.all()
        
#         # Render the updated cart HTML
#         cart_html = render_to_string('order/shopping-item.html', {'order_items': order_items, 'order': order})
#         return HttpResponse(cart_html)
    
#     return HttpResponse(status=204)


def cart_item_update(request, product_id):
    action = request.GET.get('action')
    product = get_object_or_404(Product, id=product_id)
    
    if request.user.is_authenticated:
        customer_profile = get_object_or_404(Profile, user=request.user)
        order, created = Order.objects.get_or_create(order_status=OrderStatus.PENDING, customer=customer_profile)
        order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
        
        if action == 'add':
            order_item.quantity += 1
        elif action == 'remove':
            if order_item.quantity > 1:
                order_item.quantity -= 1
            else:
                order_item.delete()
        
        order_item.save()
        
        # Re-fetch the order items to get the updated list
        order_items = order.orderitem_set.all()
        
        # Render the updated cart HTML
        
        cart_html = render_to_string('order/shopping-item.html', {
            'order_items': order_items,
            'order': order,
            'order_item': order_item  # Pass the order_item to the template
        })
        return HttpResponse(cart_html)
    
    return HttpResponse(status=204)