from .views import Home
from django.urls import path,include

urlpatterns = [
    path('', Home.as_view()),
]
