from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): # adicionar isso
        return (self.title) # resolvi o erro só colocando um parenteses
    
    class Meta:  # adicionar isso
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['id']