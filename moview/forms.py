from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from moview.models import Moviews

class UserForm(UserCreationForm):   # 장고의 UserCreationForm 클래스 상속
    email = forms.EmailField()  # 이메일 속성 추가
    
    class Meta:
        model = User
        fields = ("username", "password1","password2","email")

class MoviewForm(forms.ModelForm):
    class Meta:
        model = Moviews
        fields = ['moviename','viewdate','moviewimg','moviewline','category','story'] # 무비폼에서 사용할 뮤비 모델의 속성