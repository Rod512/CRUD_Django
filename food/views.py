from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='register')
def food_recipes(request):
    if request.method == 'POST':
        data = request.POST
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')

        Recipe.objects.create(
            recipe_image=recipe_image,
            recipe_name=recipe_name,
            recipe_description=recipe_description,
        )
        return redirect('/')
    query_set = Recipe.objects.all()

    if request.GET.get('search'):
        query_set = query_set.filter(recipe_name__icontains=request.GET.get('search'))


    context = {'food_recipes': query_set}
    return render(request, 'recipes.html',context)

def update_recipes(request,id):
    quary_set = Recipe.objects.get(id=id)

    if request.method == 'POST':
        data = request.POST
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')

        quary_set.recipe_name = recipe_name
        quary_set.recipe_description = recipe_description

        if recipe_image:
            quary_set.recipe_image = recipe_image
        
        quary_set.save()
        return redirect('/')



    context = {'food_recipes': quary_set}
    return render(request, 'update_recipes.html', context)



def delete_recipes(request, id):
    quary_set = Recipe.objects.get(id=id)
    quary_set.delete() 
    return redirect('/')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,'invalid username')
            return redirect('/login')

        user = authenticate(username = username, password = password)
        if user is None:
            messages.error(request, 'invalid password')
            redirect('/login')
        else:
            login(request,user)
            return redirect('/')

    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login')


def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "username already taken")
            return redirect('/register')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user.set_password(password)
        user.save()
        messages.info(request, "account created succesfully")
        return redirect('/register')

    return render(request, 'register.html')




