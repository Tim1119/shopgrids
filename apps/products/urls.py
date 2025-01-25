from .views import HomeView,ProductDetailView
from django.urls import path,include

app_name="products"

urlpatterns = [
    path('', HomeView.as_view()),
    path('product-detail/<str:slug>/', ProductDetailView.as_view(),name='product-details'),
]
