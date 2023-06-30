from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, BaseUserCreationForm

# from .forms import UserCreateForm, SignUpForm
from .forms import SignUpForm, UserCreateForm

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
            return redirect('index')        # 회원가입 완료시 노출 페이지 - 홈화면
            
        else:
            # 리다이렉트
            return redirect('accounts:signup')      # 회원가입 실패시 노출 페이지 - 회원가입화면
    
        
# 로그인
def login_view(request):
    # GET, POST 분리
    if request.method == 'GET' :
        # HTML 파일 응답
        pass    # 문법적 오류를 피하기 위한 임의의 예약어. 나중에 수정할 것임
    # else:
    #     request.POST.get('usrname')
    #     if username == '' or username == None:
    #         pass
        
    #     user = User.objects.get(username=username)
    #     if user == None:
    #         pass
        
    #     password = request.POST.get('password')
    # 데이터 유효성 검사
    # 비즈니스 로직 처리 
    # 응답
    