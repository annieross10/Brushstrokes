from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator


#Artwork Model
class Artwork(models.Model):
    title = models.CharField(max_length=200, unique=True)
    artist = models.CharField(max_length=100)
    created_on = models.DateTimeField()
    description = models.TextField()
    medium = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    size = models.CharField(max_length=50, default='') 
    year_created = models.PositiveIntegerField(default=timezone.now().year, 
    validators=[MaxValueValidator(limit_value=2023, message="Year created cannot exceed 2023.")]
    )
    STATUS_CHOICES = (
        ('For Sale', 'For Sale'),
        ('SOLD', 'SOLD'),
    )
    sold = models.CharField(max_length=8, choices=STATUS_CHOICES, default='For Sale') 
    slug = models.SlugField(unique=True)
    saved_by = models.ManyToManyField(User, related_name='saved_artworks', blank=True)
    STATUS_CHOICES = (
        (0, 'Draft'),
        (1, 'Published'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    def save(self, *args, **kwargs):
        current_year = timezone.now().year
        if self.year_created > current_year:
            raise ValidationError("Year created cannot exceed the current year.")
        super(Artwork, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('artwork_detail', args=[str(self.slug)])
    
    class Meta:
        verbose_name = "Artwork"
        verbose_name_plural = "Artworks"

    def __str__(self):
        return self.title
    

#Comment Model
class Comment(models.Model):
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=None)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'Comment by {self.user.username} on {self.artwork}'
    

#ContactForm Model
class ContactFormSubmission(models.Model):
    name = models.CharField(max_length=255, default="Anonymous")
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact Form Submission by {self.name}"