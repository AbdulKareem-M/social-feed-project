from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import View,ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 5
class PostDetailView(View):
    def get(self, request, **kwargs):
        id = kwargs.get('pk')
        post = Post.objects.get(id=id)
        return render(request,'post_detail.html',{'post':post})

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["content", "image"]
    template_name = "post_form.html"
    success_url = reverse_lazy("post_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["content", "image"]
    template_name = "post_form.html"
    success_url = reverse_lazy("post_list")

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "post_confirm_delete.html"
    success_url = reverse_lazy("post_list")
    
    

class CommentCreateView(LoginRequiredMixin,View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = CommentForm()
        return render(request, 'post_detail.html', {'post':post, 'form':form})
    
    
    def post(self, request,pk):
        post = get_object_or_404(Post,pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment  = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=pk)   # redirect back to the post detail page
        return render(request, 'post_detail.html', {'post':post, 'form':form})
         

