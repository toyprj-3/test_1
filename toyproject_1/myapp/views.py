from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")    # 임시 홈 화면 