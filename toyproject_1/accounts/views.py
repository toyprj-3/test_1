from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, BaseUserCreationForm, AuthenticationForm

# from .forms import UserCreateForm, SignUpForms
from .forms import SignUpForm, UserCreateForm

from users.models import User

# Create your views here.
def signup_view(request):
    
    #GET 요청 시 HTML 응답
    if request.method == "GET":
        form = SignUpForm # 데이터 입력받는 폼        
        context = { 'form': form }
        return render(request, 'accounts/signup.html', context )
    else:
    # POST 요청시 데이터 확인 후 회원 생성
        form = SignUpForm(request.POST) # (데이터유효성검사)
        
        if form.is_valid():             # (데이터유효성검사)
            # 회원가입처리 가능
            instance = form.save()
            return redirect('myapp:list')        # 회원가입 완료시 노출 페이지 - 홈화면
            
        else:
            # 리다이렉트
            return redirect('accounts:signup')      # 회원가입 실패시 노출 페이지 - 회원가입화면
    
        
# 로그인
def login_view(request):
    # GET, POST 분리
    if request.method == 'GET' :
        # HTML 파일 응답
        return render(request, 'accounts/login.html', {'form': AuthenticationForm()})
    else:
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 비즈니스 로직 처리
            login(request, form.user_cache) # 로그인 되어있는 유저라면
            #응답
            return redirect('myapp:list')
            
        else:
            # 비즈니스 로직 처리 - 로그인 실패
            # 응답 
            return render(request, 'accounts/login.html', {'form': form})