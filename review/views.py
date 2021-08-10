from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from review.models import Post
from wine.models import Wine
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
    owner = request.GET.get('owner')
    selected_wine = []
    if wine:
      self.queryset = Post.objects.filter(wine=wine)
      selected_wine = Wine.objects.get(pk=wine)
    elif owner:
      self.queryset = Post.objects.filter(owner=owner)
    # 리뷰가 등록된 와인
    reviewd_wines = set()
    for post in Post.objects.all():
      reviewd_wines.add(post.wine)
    self.extra_context = {
      'reviewd_wines': reviewd_wines,
      'selected_wine': selected_wine
    }
    return super().get(request, *args, **kwargs)

class PostDetailView(DetailView):
  context_object_name = 'post'
  model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
  model = Post
  fields = ['wine', 'title', 'content', 'rating']
  success_url = reverse_lazy('review:index')

  def get(self, request, *args, **kwargs):
    self.wine_id = request.GET.get('wine')
    if self.wine_id:
      self.initial = { 'wine': Wine.objects.get(pk=self.wine_id) }
    return super().get(request, *args, **kwargs)

  def form_valid(self, form):
    form.instance.owner = self.request.user
    return super().form_valid(form)

class PostUpdateView(OwnerOnlyMixin, UpdateView):
  model = Post
  fields = ['wine', 'title', 'content', 'rating']
  success_url = reverse_lazy('review:index')

class PostDeleteView(OwnerOnlyMixin, DeleteView) :
  model = Post
  success_url = reverse_lazy('review:index')
  
  def get(self, *args, **kwargs):
    return self.post(*args, **kwargs)
