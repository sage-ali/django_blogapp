from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

    
    path('post/<int:pk>/delete', login_required(views.BlogDeleteView.as_view()), name = 'delete_post'),
    path('post/<int:pk>/edit', login_required(views.BlogUpdateView.as_view()), name = 'edit_post'),
    path('post/new/', login_required(views.BlogCreateView.as_view()), name = 'new_post'),
    path('post/<int:pk>', views.BlogDetailView.as_view(), name = 'post_details'),
    
    path('', views.BlogListView.as_view(), name = 'blogapp-home'),
    
    
    path("password_reset", views.password_reset_request, name="password_reset"),
    
    # path('reset_password/',
    #     auth_views.PasswordResetView.as_view(template_name="password/password_reset.html"),
    #     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_form.html"), 
        name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password/password_reset_done.html"), 
        name="password_reset_complete"),

]