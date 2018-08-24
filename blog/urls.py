from django.urls import path, include,re_path
from .views import *
app_name = 'blog'
urlpatterns = [
    path('', BlogPostClassView.as_view(), name="index")
]