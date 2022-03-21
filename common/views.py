from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from moview.forms import UserForm

# Create your views here.
def signup(request):
    # 계정 생성
    if request.method == "POST": # 입력한 후이면
        form = UserForm(request.POST)
        if form.is_valid(): # 유효성 검사?
            form.save()
            # form.cleaned_data.get : 입력값을 개별적으로 얻고 싶은 경우에 사용
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get("password1")
            # 사용자명과 비밀번호가 정확한지 검증
            user = authenticate(username=username, password=raw_password)
            # 자동으로 로그인하기
            login(request,user)
            return redirect('/')    # url이름이 index인 곳으로 이동시킴
    else:
        form = UserForm()
    return render(request, 'common/signup.html',{'form':form})