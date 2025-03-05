from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.models import Post

class HomeView(ListView, LoginRequiredMixin):
  model = Post
  template_name = 'home.html'
  context_object_name = 'posts'
  ordering = ['-created_at']
  login_url = 'login'

