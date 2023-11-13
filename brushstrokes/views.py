from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.db.models import Q
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import ContactForm, CommentForm
from .models import Artwork, Comment, ContactFormSubmission
from datetime import datetime
from django.contrib import messages
from django.contrib.messages import get_messages

# Base
def your_view(request):
    current_year = datetime.now().year
    return render(request, 'base.html', {'year': current_year})

# Index
def index(request):
    return render(request, 'index.html')

# About
def about_view(request):
    return render(request, 'about.html')

# Contact
def contact_view(request):
    return render(request, 'contact.html')

# Gallery
def gallery_view(request):
    artworks = Artwork.objects.filter(status=1)  
    print(artworks)
    
    return render(request, 'gallery.html', {'artworks': artworks})

# Contact Form
@csrf_protect
@require_http_methods(["GET", "POST"])
def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            contact_submission = ContactFormSubmission(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            contact_submission.save() 

            messages.success(request, 'Thank you for your email! We will get back to you as soon as we can.', extra_tags='contact-form')

            return redirect('contact')

    else:
        storage = get_messages(request)
        for message in storage:
            pass
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

# Artwork 
class ArtworkDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Artwork.objects.filter(status=1)
        artwork = get_object_or_404(queryset, slug=slug)
        comments = Comment.objects.filter(artwork=artwork, approved=True).order_by('created_on')
        comment_form = CommentForm()

        return render(
            request,
            "artwork_detail.html",
            {
                "comment_form": comment_form,
                "artwork": artwork,
                "comments": comments
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Artwork.objects.filter(status=1)
        artwork = get_object_or_404(queryset, slug=slug)

        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user 
            comment.artwork = artwork
            comment.approved = False
            comment.save()
            return JsonResponse({'success': True})

        return JsonResponse({'success': False}) 

# Delete Comment
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user == comment.user:
        comment.delete()

    return redirect('artwork_detail', slug=comment.artwork.slug)

# Artwork List
class ArtworkList(ListView):
    model = Artwork
    queryset = Artwork.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'artworks'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# User Acount
@login_required
def user_account(request):
    user = request.user  
    context = {
        'user': user,
    }
    return render(request, 'account/user_account.html', context)

# Search for Artwork
def search_view(request):
    query = request.GET.get('q', '')
    artworks = Artwork.objects.all()

    if query:
        artworks = artworks.filter(
            Q(title__icontains=query) |
            Q(medium__icontains=query) |
            Q(artist__icontains=query)
        )
    context = {
        'artworks': artworks,
        'search_query': query, 
    }
    return render(request, 'gallery.html', context)

# Save Artwork
@login_required
def save_artwork(request, artwork_id):
    artwork = get_object_or_404(Artwork, id=artwork_id)
    user = request.user

    if artwork.saved_by.filter(id=user.id).exists():
        artwork.saved_by.remove(user)
        saved = False
    else:
        artwork.saved_by.add(user)
        saved = True

    return JsonResponse({'saved': saved})

# Remove Artwork
@login_required
def remove_artwork(request, artwork_id):
    artwork = get_object_or_404(Artwork, id=artwork_id)
    user = request.user

    if artwork.saved_by.filter(id=user.id).exists():
        artwork.saved_by.remove(user)
        saved = False
    else:
        saved = True

    return JsonResponse({'saved': saved})


