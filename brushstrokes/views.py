from .forms import ContactForm, CommentForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Artwork, Comment
from .models import ContactFormSubmission
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.shortcuts import render, redirect
from datetime import datetime
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.messages import get_messages

class ArtworkList(ListView):
    model = Artwork
    queryset = Artwork.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'artworks'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

def your_view(request):
    current_year = datetime.now().year
    return render(request, 'base.html', {'year': current_year})

def index(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

def gallery_view(request):
    return render(request, 'gallery.html')

def contact_view(request):
    return render(request, 'contact.html')

def gallery_view(request):
    artworks = Artwork.objects.filter(status=1)  
    print(artworks)
    
    return render(request, 'gallery.html', {'artworks': artworks})


class ArtworkDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Artwork.objects.filter(status=1)
        artwork = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "artwork_detail.html",
            {

                "artwork": artwork,
            },)
    

    def post(self, request, slug, *args, **kwargs):
        queryset = Artwork.objects.filter(status=1)
        artwork = get_object_or_404(queryset, slug=slug)    

        return redirect('artwork-detail', slug=slug)
    


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

            messages.success(request, 'Thank you for your email! We will get back to you as soon as we can.')

            return redirect('contact')

    else:
        storage = get_messages(request)
        for message in storage:
            pass
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
