from django.shortcuts import render,redirect
from .models import *

def food_recipes(request):
    if request.method == 'POST':
        data = request.POST
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')

        Recipe.objects.create(
            recipe_image = recipe_image,
            recipe_name = recipe_name,
            recipe_description = recipe_description,
        )
        return redirect('/')
    query_set = Recipe.objects.all()

    if request.GET.get('search'):
       query_set = query_set.filter(recipe_name__icontains = request.GET.get('search'))


    context = {'food_recipes': query_set}
        
    return render(request, 'recipes.html',context)

def update_recipes(request,id):
    quary_set = Recipe.objects.get(id = id)

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
    quary_set = Recipe.objects.get(id = id)
    quary_set.delete() 
    return redirect('/')




