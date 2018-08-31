from django.urls import path, include,re_path
from .views import *
app_name = 'blog'



urlpatterns = [
    path('',
         BlogPostClassView.as_view(),
         name="index"),
    path('tag/<str:tagname>',
         taglistview,
         name='tag'),
    path('<int:year>/<int:month>/<int:day>/<str:slug>',
         postView,
         name='post'),
    path('cat/<str:slug>',
         catlistview,
         name='categories'),
]