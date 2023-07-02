from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, BaseUserCreationForm


from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)
from .models import Post


# Create your views here.
# class post_detail_view(DetailView, id):
# model = Post
# def post_list(request):
#   return render(request, "list.html")


# def post_detail(request, pk):
#   post = Post.objects.get(pk=pk)
#  return render(request, "detail.html")


class PostList(ListView):
    model = Post
    ordering = "-pk"
    template_name = "myapp/main.html"


class PostDetail(DetailView):
    model = Post
    template_name = "myapp/More.html"


class PostUpdate(UpdateView):
    model = Post
    template_name = "myapp/fix.html"
    fields = ["title", "content", "image"]


class PostCreate(CreateView):
    model = Post
    fields = ["title", "content", "image"]
    template_name = "myapp/create.html"


class PostDelete(DeleteView):
    model = Post
    success_url = "/"


# def post_delete(request, id):
