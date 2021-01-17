from django.shortcuts import render, HttpResponse, redirect
from .models import User
from .forms import RegisterForm, LoginForm

# Create your views here.


def index(request):
    user_id = request.session.get('user')

    if user_id:
        user = User.objects.get(pk=user_id)
        return render(request, 'user/index.html', {'email' : user.email})

    return render(request, 'user/index.html')


def register(request):
    # POST(사용자가 정보를 입력했을 때)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        # 유효성 검사 성공(문제 없음)시
        if form.is_valid():
            user = User(
                name=form.data.get('name'), 
                email=form.data.get('email'), 
                password=form.data.get('password')
            )

            user.save()

            return redirect('/')
        # 유효성 검사 실패시
        else:
            # render 함수를 통해 뷰와 템플릿을 연결하고 템플릿에 정보를 넘겨줄 수 있음
            return render(request, "user/register.html", {'form': form})
    # GET(사용자가 처음 들어와 아직 정보를 입력하기 전)
    else:
        form = RegisterForm()
        return render(request, "user/register.html", {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()

    return render(request, 'user/login.html', {'form': form})

def board_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/board/write')
    else:
        form = LoginForm()

    return render(request, 'user/board_login.html', {'form': form})


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')
