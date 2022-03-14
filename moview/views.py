import random
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
    # 랜덤으로 배경 스타일 주기
    style = ['style1','style2','style3','style4','style5','style6']
    randoms = list()
    for i in range(len(mlist)):
        randoms.append(random.choice(style))
    context = {'multilist' : zip(mlist,style)}
    return render(request, 'moview/index.html', context)

def add_movie(request):
    # 뮤비 추가
    if request.method == 'POST':
        form = MoviewForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.uploaduser = request.user.username
            movie.moviewimg = request.FILES.get('moviewimg')
            movie.save()
            return redirect('moview:index')
    else:
        form = MoviewForm()
    context = {'form':form}
    return render(request, 'moview/add.html',context)


def movie_detail(request, movie_id):
    # 해당 영화일기의 내용 출력 : pk - 해당 아이디인것만 가져오기
    movies = get_object_or_404(Moviews, pk=movie_id)
    lines = list(movies.story.split('\n'))      # 문단 끊어서 보내기
    is_user = request.user.username== movies.uploaduser     # 지금 로그인된 유저가 작성한 게시물인지
    context = {'moview': movies, 'lines':lines, 'is_user':is_user}
    return render(request, 'moview/generic.html', context)


def movie_delete(request):
    return None


def movie_update(request):
    return None