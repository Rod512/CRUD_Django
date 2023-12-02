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
    context = {'food_recipes': query_set}
        
    return render(request, 'recipes.html',context)

def delete_recipes(request, id):
    quary_set = Recipe.objects.get(id = id)
    quary_set.delete() 
    return redirect('/')


