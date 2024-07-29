from django.urls import path 
# from django.conf import settings
from django.conf.urls.static import static
from .views import (
    LoginView,
    RegisterView,
)

urlpatterns = [
    path("", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
]