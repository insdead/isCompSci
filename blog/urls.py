from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import PostListView, PostDetailView


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('blog/', PostListView.as_view(), name='blog-blog'),
    path('resume/', views.resume, name='blog-resume'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
] 
