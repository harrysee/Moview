from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Moviews
from .forms import MoviewForm

# render : 파이썬 데이터를 템플릿에 적용하여 HTML로 반환하는 함수
# Create your views here.
def index(request):
    # 영화목록 출력
    # order_by : viewdate순으로 -붙여서 역방향
    mlist = Moviews.objects.order_by('-viewdate')
    # moview 데이터를 moview.index.html에 적용하여 HTML 리턴함
    context = {'mlist' : mlist}
    return render(request, 'moview/index.html',context)

def add_movie(request):
    # 뮤비 추가
    if request.method == 'POST':
        form = MoviewForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('moview:index')
    else:
        form = MoviewForm()
    context = {'form':form}
    return render(request, 'moview/add.html',context)