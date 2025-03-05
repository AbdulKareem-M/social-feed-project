from django.views.generic import ListView
from posts.models import Post

class HomeView(ListView):
  model = Post
  template_name = 'home.html'
  context_object_name = 'posts'
  ordering = ['-created_at']

