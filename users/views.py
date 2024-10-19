from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from django.contrib.auth.views import LogoutView

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
    context = {'form': form}
    return render(request, 'registration/register.html', context)

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('learning:index')  # Redirect to the index page after logout
    # Handle GET request by rendering a confirmation page
    return render(request, "learning/logout.html")

#class PatchLogoutView(LogoutView):
    #http_method_names = ["get", "post", "options"]
    #def get(self, request, *args, **kwargs):
        #return self.post(request, *args, **kwargs)