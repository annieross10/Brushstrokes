from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField


class Artwork(models.Model):
    title = models.CharField(max_length=200, unique=True)
    artist = models.CharField(max_length=100)
    created_on = models.CharField(max_length=200)
    description = models.TextField()
    medium = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    size = models.CharField(max_length=50, default='') 
    year_created = models.PositiveIntegerField(default=timezone.now().year) 
    STATUS_CHOICES = (
        ('For Sale', 'For Sale'),
        ('SOLD', 'SOLD'),
    )
    sold = models.CharField(max_length=8, choices=STATUS_CHOICES, default='For Sale') 
    slug = models.SlugField(unique=True)
    status = models.IntegerField(default=1)
    saved_by = models.ManyToManyField(User, related_name='saved_artworks', blank=True)
    
    def save(self, *args, **kwargs):
        current_year = timezone.now().year
        if self.year_created > current_year:
            raise ValidationError("Year created cannot exceed the current year.")
        super(Artwork, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('artwork_detail', args=[str(self.slug)])
    

class Comment(models.Model):
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'Comment by {self.name} on {self.artwork}'
    

class ContactFormSubmission(models.Model):
    name = models.CharField(max_length=255, default="Anonymous")
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact Form Submission by {self.name}"