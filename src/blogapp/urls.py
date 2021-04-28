from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

    
    path('post/<int:pk>/delete', login_required(views.BlogDeleteView.as_view()), name = 'delete_post'),
    path('post/<int:pk>/edit', login_required(views.BlogUpdateView.as_view()), name = 'edit_post'),
    path('post/new/', login_required(views.BlogCreateView.as_view()), name = 'new_post'),
    path('post/<int:pk>', views.BlogDetailView.as_view(), name = 'post_details'),
    
    path('', views.BlogListView.as_view(), name = 'blogapp-home'),
]