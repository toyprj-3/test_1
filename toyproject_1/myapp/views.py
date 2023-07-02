
from typing import Any
from django import http
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)
from django.core.exceptions import PermissionDenied
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


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "myapp/fix.html"
    fields = ["title", "content", "image"]

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else :
            raise PermissionDenied



class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content", "image"]
    template_name = "myapp/create.html"

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('myapp:list')

def PostDelete(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect("myapp:list")