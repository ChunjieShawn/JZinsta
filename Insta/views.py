from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from Insta.models import Post
from django.urls import reverse_lazy

# Create your views here.

class HelloDjango(TemplateView):
    template_name = 'home.html'

class PostView(ListView):
    #find all the Post objects in db and return in object_list
    model = Post
    template_name = 'posts.html'

class PostDetail(DetailView):
    model = Post
    template_name = "postDetail.html"

class PostCreateView(CreateView):
    model = Post
    template_name = "makePost.html"
    fields = '__all__'

class PostUpdateView(UpdateView):
    model = Post
    template_name = "updatePost.html"
    fields = ('title',)

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'deletePost.html'
    success_url = reverse_lazy('home')