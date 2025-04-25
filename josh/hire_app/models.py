from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class Outfit(models.Model):
    category = models.ForeignKey(Category, related_name='clothes', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    is_hired = models.BooleanField(default=False)
    image = models.ImageField(upload_to='outfit_images',blank=True)
    hiring_price=models.IntegerField()
    description = models.TextField(blank=True)
    # created_by = models.ForeignKey(User, related_name='belong', on_delete=models.CASCADE, null=True)
    # created_on = models.DateTimeField(auto_now_add=True,null=True)

    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name