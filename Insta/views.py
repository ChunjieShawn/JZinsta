from django.views.generic import TemplateView, ListView, DetailView

from Insta.models import Post

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