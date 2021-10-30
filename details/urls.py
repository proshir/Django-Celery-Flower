from collections import defaultdict
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
app_name="details"
urlpatterns=[
    path('authors/',views.AuthorList.as_view(),name="Authors"),
    path('books/',views.BookList.as_view(),name="Books"),
    path('author/<int:pk>/',views.AuthorDetail.as_view(),name="Author"),
    path('book/<int:pk>/',views.BookDetail.as_view(),name="Book"),
    path('bookucs/',views.BookUCS.as_view(),name="Book Update Or Create")
]
