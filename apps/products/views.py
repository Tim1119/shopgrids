from django.shortcuts import render
from django.views.generic import TemplateView
# from django.contrib.
from apps.category.models import Category
from apps.products.models import Product
from apps.brands.models import Brand
# Create your views here.
class Home(TemplateView):
    template_name = 'products/product_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch all categories and prefetch related subcategories in one query
        categories = Category.objects.prefetch_related('subcategories').all()
        category_data = []
        for category in categories:
            category_data.append({'category': category,'subcategories': category.subcategories.all()})

        trending_products = Product.objects.filter(is_trending=True,is_active=True)[:10]
        special_offer_products = Product.objects.filter(is_special_offer=True,is_active=True)[:10]
        product_brands = Brand.objects.all()
        
        

        context['category_data'] = category_data
        context['trending_products'] = trending_products
        context['special_offer_products'] = special_offer_products
        context['product_brands'] = product_brands
        return context