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
    login_required = True
    model = Post
    template_name = 'newpost.html'
    fields = ['title', 'author', 'body']
    
class BlogUpdateView(UpdateView):
    login_required = True
    model = Post
    template_name = 'editpost.html'
    fields = ['title', 'body']
    
class BlogDeleteView(DeleteView):
    login_required = True
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blogapp-home')