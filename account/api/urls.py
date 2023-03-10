from django.urls import path
from account.api import views as account_views

urlpatterns = [
    path("register/",account_views.RegisterView.as_view())
]