from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Moviews

# render : 파이썬 데이터를 템플릿에 적용하여 HTML로 반환하는 함수
# Create your views here.
def index(request):
    # 영화목록 출력
    # order_by : viewdate순으로 -붙여서 역방향
    mlist = Moviews.objects.order_by('-viewdate')
    # moview 데이터를 moview.index.html에 적용하여 HTML 리턴함
    context = {'mlist' : mlist}
    return render(request, 'moview/index.html',context)

def addmovie(request):
    mlist = Moviews.objects.order_by('-viewdate')
    # moview 데이터를 moview.index.html에 적용하여 HTML 리턴함
    context = {'mlist': mlist}
    return render(request, 'moview/add.html',context)