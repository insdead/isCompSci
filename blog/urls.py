from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('blog/', views.blog, name='blog-blog'),
    path('resume/', views.resume, name='blog-resume'),
    path('article/', views.article, name='blog-article'),
] 
