from django.urls import path, include
from . import views
from learning.views import logout_view


app_name = 'users'
urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
    # Registration page.
    path('register/', views.register, name='register'),
    path('logout/', logout_view, name='logout'),
    #path('logout/', views.PatchLogoutView.as_view(next_page='login'), name='logout'),
]
    

