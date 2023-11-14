from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from allauth.account.views import SignupView

urlpatterns = [
    path('', views.index_view, name='index'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_form, name='contact'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('search/', views.search_view, name='search'),
    path('user_account/', views.user_account, name='user_account'),
    path('save-artwork/<int:artwork_id>/', views.save_artwork, name='save_artwork'),
    path('remove-artwork/<int:artwork_id>/', views.remove_artwork, name='remove_artwork'),
    path('delete-comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('<slug:slug>/', views.ArtworkDetail.as_view(), name='artwork_detail'),
    path('artwork/<slug:slug>/', views.ArtworkDetail.as_view(), name='artwork-detail'),

]