from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from review.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from accounts.views import OwnerOnlyMixin

class PostListView(ListView):
  model = Post
  template_name = 'review/post_all.html'
  context_object_name = 'posts'
  paginate_by = 5

  def get(self, request, *args, **kwargs):
    wine = request.GET.get('wine')
    if wine:
      self.queryset = Post.objects.filter(wine=wine)
    return super().get(request, *args, **kwargs)

class PostDetailView(DetailView):
  model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
  model = Post
  fields = ['title', 'content']
  success_url = reverse_lazy('review:index')
  
  def form_valid(self, form):
    form.instance.owner = self.request.user
    return super().form_valid(form)

class PostUpdateView(OwnerOnlyMixin, UpdateView):
  model = Post
  fields = ['title', 'content']
  success_url = reverse_lazy('review:index')

class PostDeleteView(OwnerOnlyMixin, DeleteView) :
  model = Post
  success_url = reverse_lazy('review:index')
  
  def get(self, *args, **kwargs):
    return self.post(*args, **kwargs)

