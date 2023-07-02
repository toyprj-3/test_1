from django.shortcuts import render
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)
# Create your views here.
#def index(request):
#    return render(request, "index.html")    # 임시 홈 화면 

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