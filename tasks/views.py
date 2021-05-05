from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.views.generic.list import ListView

# Create your views here.


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('list')
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
		return render(request, 'tasks/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('list')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('list')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'tasks/login.html', context)

def logoutUser(request):
        logout(request)
        return redirect('login')


@login_required(login_url='login')
def index(request):

    tasks = Task.objects.filter(user=request.user) # to get tasks for specific user
    form = TaskForm()

    #user = User.objects.get(id = pk)    # get the name of user
    #task = Task.objects.filter
    #form = TaskForm(instance = task)

    if request.method == "POST":   
        form = TaskForm(request.POST)       # http POST is when you create the task
        # user = request.user / using user.id would be better 
        # user could have same name

        if form.is_valid():    # check email add format, etc  
            task = form.save(commit = False)
            task.user = request.user
            task.save()
         
        return redirect('/') # -> this need to be returned following page id

    context = {'tasks':tasks, 'form':form}

    return render(request, 'tasks/list.html', context)


@login_required(login_url='login')
def updateTask(request, pk):

    task = Task.objects.get(id=pk)
    form = TaskForm(instance = task) #task from the above line

    if request.method =="POST":
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():    
            form.save()
        return redirect('/')            # / -> homepage 

    context = {'form': form}

    return render(request, 'tasks/update_task.html', context)

@login_required(login_url='login')
def deleteTask(request, pk):

    task = Task.objects.get(id = pk)

    if request.method =="POST":
        task.delete()
        return redirect('/')

    context = {'task':task}

    return render(request, 'tasks/delete.html', context)