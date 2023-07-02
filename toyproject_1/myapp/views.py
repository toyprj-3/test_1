
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
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
    fields = ["title", "content", "image", "author"]



class PostCreate(CreateView):
    model = Post
    fields = ["title", "content", "image", "author"]
    template_name = "myapp/create.html"

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('myapp:list')

def PostDelete(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == "GET":
        context = {'post': post}
        return render(request, "myapp/delete.html", context)
    else:
        post.delete()
        return redirect("myapp:list")