from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, BaseUserCreationForm

class UserBaseForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'
        
        
class UserCreateForm(UserBaseForm):
# class BaseUserCreationForm(UserBaseForm):
    password2 = forms.CharField(widget=forms.PasswordInput()) 
    # password = forms.CharField(error_messages={"required" : "비밀번호를 입력해주세요."}, widget=forms.PasswordInput()) 
    class Meta(UserBaseForm.Meta):
        fields = [
            'username', 
            'email', 
            'phone', 
            'password',
            'password2',
        ]      
        
class SignUpForm(UserCreationForm):
# class SignUpForm(BaseUserCreationForm):
    class Meta(UserCreationForm.Meta):
    # class Meta(BaseUserCreationForm.Meta):
        model = get_user_model()
        # fields = ['username', 'email', 'password']
        fields = [
            'username', 
            'email',
        ]