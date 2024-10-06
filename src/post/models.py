from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify
from django.db import models
from PIL import Image

user = get_user_model()

class BlogPost(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Titre')
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    author = models.ForeignKey(user, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Auteur')
    last_updated = models.DateTimeField(auto_now=True, verbose_name='Dernière mise à jour')
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='Créé le')
    content = models.TextField(blank=True, verbose_name='Contenu')
    thumbnail = models.ImageField(upload_to='blog', blank=True, null=True, verbose_name='Miniature')
    published = models.BooleanField(default=False, verbose_name='Publié')
    

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        
        # Resize the thumbnail if needed
        if self.thumbnail:
            img = Image.open(self.thumbnail)
            if img.height > 600 or img.width > 600:
                output_size = (600, 600)
                img.thumbnail(output_size)
                img.save(self.thumbnail.path)
                
        super().save(*args, **kwargs)

    @property
    def author_or_default(self):
        return self.author.username if self.author else 'Auteur inconnu'

    def get_absolute_url(self):
        return reverse("post:home")
