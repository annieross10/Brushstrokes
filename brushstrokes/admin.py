from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin 
from .models import Artwork, Comment, ContactFormSubmission

# Define the Artwork admin
class ArtworkAdmin(SummernoteModelAdmin):
    list_display = ('title', 'artist', 'year_created', 'sold', 'created_on')
    list_filter = ('year_created', 'sold')
    search_fields = ('title', 'artist')
    prepopulated_fields = {'slug': ('title',)}  
    summernote_fields = ('description',)  

admin.site.register(Artwork, ArtworkAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'artwork', 'created_on', 'approved')
    list_filter = ('approved',)
    search_fields = ('name', 'artwork__title') 

admin.site.register(Comment, CommentAdmin)

class ContactFormSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')

admin.site.register(ContactFormSubmission, ContactFormSubmissionAdmin)