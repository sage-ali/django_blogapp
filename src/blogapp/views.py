from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.urls import reverse_lazy

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .models import Post

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import CreateUserForm


from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

def password_reset_request(request):
	if request.method == "POST":
		
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			
			if associated_users.exists():
				
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password/password_reset.txt"
					c = {
						"email":user.email,
						'domain':'127.0.0.1:8000',
						'site_name': 'Website',
						"uid": urlsafe_base64_encode(force_bytes(user.pk)),
						"user": user,
						'token': default_token_generator.make_token(user),
						'protocol': 'http',
					}
    
					email = render_to_string(email_template_name, c)
					
					try:
						return redirect(email)
					except:
						return HttpResponse('Try again')
					# return redirect ("reset_password_complete/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password/password_reset.html", context={"password_reset_form":password_reset_form})

# Create your views here.


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('blogapp-home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'accounts/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('blogapp-home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('blogapp-home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('blogapp-home')


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    
class BlogCreateView(CreateView):
    model = Post
    template_name = 'newpost.html'
    fields = ['title', 'author', 'body']
    
class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'editpost.html'
    fields = ['title', 'body']
    
class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blogapp-home')