from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView

urlpatterns = [
    path('post/<int:pk>/edit', BlogUpdateView.as_view(), name = 'edit_post'),
    path('post/new/', BlogCreateView.as_view(), name = 'new_post'),
    path('post/<int:pk>', BlogDetailView.as_view(), name = 'post_details'),
    path('', BlogListView.as_view(), name = 'blogapp-home'),
]