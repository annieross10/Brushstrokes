from django.contrib import admin
from django.utils.html import format_html
from .models import Artwork, Comment, ContactFormSubmission

# Define the Artwork admin
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'year_created', 'sold', 'created_on')
    list_filter = ('year_created', 'sold', 'status')
    search_fields = ('title', 'artist', 'status')
    prepopulated_fields = {'slug': ('title',)}  

admin.site.register(Artwork, ArtworkAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'artwork', 'created_on', 'approved')
    list_filter = ('approved',)
    search_fields = ('artwork__title', 'artwork__artist') 

admin.site.register(Comment, CommentAdmin)

class ContactFormSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')

admin.site.register(ContactFormSubmission, ContactFormSubmissionAdmin)