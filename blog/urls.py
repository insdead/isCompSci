from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('blog/', views.blog, name='blog-blog'),
    path('resume/', views.resume, name='blog-resume'),
]
