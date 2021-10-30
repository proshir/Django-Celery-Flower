
from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.LoginPage.as_view(), name='login'),
    path('logout/', views.LogoutPage.as_view(), name='logout'),

]
