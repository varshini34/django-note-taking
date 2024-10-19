from django.urls import path
from . import views
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from .views import logout_view

app_name = 'learning'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topics.
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    
    
]

def custom_404(request, exception):
    return render(request, '404.html', status=404)

handler404 = 'your_app.views.custom_404'