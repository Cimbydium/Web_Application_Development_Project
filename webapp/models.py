from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=180)
    creator = models.CharField(max_length=45)
    category = models.CharField(max_length=35)
    prep_time = models.IntegerField()
    instructions = models.TextField()
    image = models.ImageField(upload_to='webapp/media/recipe_images/', blank=True, null=True)

    def __str__(self):
        return self.title
    
class Review(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} on {self.recipe.title}"
