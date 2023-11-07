from django.shortcuts import render
from .models import Artwork
from django.views.generic import ListView
from datetime import datetime


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

class ArtworkList(ListView):
    model = Artwork
    queryset = Artwork.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'artworks'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context