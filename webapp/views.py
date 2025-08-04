
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import Recipe
from .forms import UserRegistrationForm, RecipeForm, ReviewForm
from django.shortcuts import redirect



# عرض الصفحة الترحيبية
def showWelcomePage(request):
    return render(request, 'webapp/welcomepage.html')


# تسجيل مستخدم جديد
def addNewUser(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('recipes')
    else:
        form = UserRegistrationForm()
    return render(request, 'webapp/register.html', {'form': form})


# عرض جميع الوصفات
@login_required
def showRecipes(request):
    recipes = Recipe.objects.all()
    return render(request, 'webapp/recipes.html', {'recipes': recipes})


# عرض تفاصيل وصفة معينة
@login_required
def showRecipeDetails(request, id):
    recipe = get_object_or_404(Recipe, pk=id)
    reviews = recipe.reviews.all().order_by('-created_at')

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.recipe = recipe
            review.user = request.user
            review.save()
            return redirect('recipe', id=recipe.id)  
    else:
        form = ReviewForm()

    return render(request, 'webapp/recipe_detail.html', {
        'recipe': recipe,
        'reviews': reviews,
        'form': form
    })


# إضافة وصفة جديدة
@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save()
            messages.success(request, f'Recipe "{recipe.title}" added successfully!')
            return redirect('recipes')
    else:
        form = RecipeForm()
    return render(request, 'webapp/add_recipe.html', {'form': form})


# تحديث وصفة
@login_required
def update_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request, 'Recipe updated successfully!')
            return redirect('recipes')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'webapp/update_recipe.html', {'form': form})


# حذف وصفة
@login_required
def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        recipe.delete()
        messages.success(request, 'Recipe deleted successfully!')
        return redirect('recipes')
    return render(request, 'webapp/delete_recipe.html', {'recipe': recipe})

def custom_logout(request):
    logout(request)
    return redirect('login')