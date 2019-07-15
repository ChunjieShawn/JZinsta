from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from Insta.models import Post, InstaUser
from Insta.forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class PostView(LoginRequiredMixin, ListView):
    #find all the Post objects in db and return in object_list
    model = Post
    template_name = 'index.html'
    login_url = 'login'

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

class SignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

class UserDetail(DetailView):
    model = InstaUser
    template_name = 'user_profile.html'

class EditProfile(UpdateView):
    model = InstaUser
    template_name = 'edit_profile.html'
    fields = ('username', 'profile_pic',)