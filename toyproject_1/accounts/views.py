from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

from .forms import UserCreateForm, SignUpForm

# Create your views here.
def signup_view(request):
    
    #GET 요청 시 HTML 응답
    if request.method == "GET":
        form = SignUpForm
        context = { 'form': form }
        return render(request, 'accounts/signup.html', context )
    else:
    # POST 요청시 데이터 확인 후 회원 생성
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            # 회원가입처리 가능
            instance = form.save()
            return redirect('index')        # 회원가입 완료시 노출 페이지
            
        else:
            # 리다이렉트
            return redirect('accounts:signup')    
            # return redirect('index')
    
        
    