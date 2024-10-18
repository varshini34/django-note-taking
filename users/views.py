from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form. 
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            login(request, new_user)
            return redirect('learning:index')
    # Display a blank or invalid form.
    c = {'form': form}
    return render(request, 'registration/register.html', c, context_instance=RequestContext(request))