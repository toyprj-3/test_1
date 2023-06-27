from django.shortcuts import render
from .forms import UserCreateForm

# Create your views here.
def signup_view(request):
    
    #GET 요청 시 HTML 응답
    if request.method == "GET":
        form = UserCreateForm
        context = { 'form': form }
        return render(request, 'accounts/signup.html', context )
    else:
        pass