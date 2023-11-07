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
    path('login/', auth_views.LoginView.as_view(template_name='account_login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('user_account/', views.user_account, name='user_account'),

    path('search/', views.search_view, name='search'),
    path('save-artwork/<int:artwork_id>/', views.save_artwork, name='save_artwork'),
    path('remove-artwork/<int:artwork_id>/', views.remove_artwork, name='remove_artwork'),
    path('<slug:slug>/', views.ArtworkDetail.as_view(), name='artwork_detail'),
    path('artwork/<slug:slug>/', views.ArtworkDetail.as_view(), name='artwork-detail'),

]