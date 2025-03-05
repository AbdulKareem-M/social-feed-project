from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, UpdateView
from .models import CustomUser
from .forms import CustomUserCreationForm,ProfileUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib import messages
from posts.models import Post

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)  # Initialize for POST
        if form.is_valid():
            user = form.save()
            messages.success(request, "Your account has been created! You can now log in.")
            return redirect('login')
    else:
        form = CustomUserCreationForm()  # Initialize for GET (display empty form)

    return render(request, "register.html", {"form": form})
    

class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_posts'] = Post.objects.filter(user = self.request.user).order_by('-created_at')
        return context
        

class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = ProfileUpdateForm
    template_name = "profile_edit.html"
    success_url = reverse_lazy("profile")  # Redirect back to profile after editing

    def get_object(self):
        return self.request.user  # Allow users to edit their own profile
    

def custom_logout(request):
    logout(request)
    return redirect('home')


