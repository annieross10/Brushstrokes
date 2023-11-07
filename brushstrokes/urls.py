from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from allauth.account.views import SignupView

urlpatterns = [
    path('', views.ArtworkList.as_view(), name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_form, name='contact'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('signup/', SignupView.as_view(), name='account_signup'),
    path('<slug:slug>/', views.ArtworkDetail.as_view(), name='artwork_detail'),
    path('artwork/<slug:slug>/', views.ArtworkDetail.as_view(), name='artwork-detail'),

]