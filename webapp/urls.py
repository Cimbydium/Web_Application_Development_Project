from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
  
    path('', views.showWelcomePage, name='welcomepage'),

   
    path('register/', views.addNewUser, name='register'),

    
    path('login/', auth_views.LoginView.as_view(template_name='webapp/login.html'), name='login'),

   
   path('logout/', views.custom_logout, name='logout'),

    
    path('recipes/', views.showRecipes, name='recipes'),

    
    path('recipe/<int:id>/', views.showRecipeDetails, name='recipe'),

    
    path('recipe/add/', views.add_recipe, name='add_recipe'),

    
    path('recipe/<int:pk>/update/', views.update_recipe, name='update_recipe'),

    
    path('recipe/<int:pk>/delete/', views.delete_recipe, name='delete_recipe'),
]
