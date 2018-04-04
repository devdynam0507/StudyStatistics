from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from .forms import UserLoginForm, CreateUserForm, StatisticsWriteForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.template.context_processors import csrf
from .util.time import getmonthdays, gettoday, getmonth, getyear, str_yearnow, get_weeks_date, fdstr
from .models import UserStudyData
from .util.modelmanage import DBManager
from .util.statistics import calc_study_time, calc_week_data, calc_week_top_data, calc_lastweek_data, calc_average_data, calc_average_hour_data, calc_getlabel, calc_average_month_data
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import date

from django.contrib.auth import (
	authenticate, get_user_model, login, logout
)

# Create your views here.
def index(request):
    calc_week_data(request.user.username)
    return render(request, 'elections/index.html')

def statistics(request):
    return render(request, 'elections/statistics.html')


# ======================================================================================================= #

#수학 통계량 보여주는 view
def statisticsview_math(request):
    week_days = get_weeks_date(0)
    calc_week = calc_week_data(request.user.username)
    top_d = calc_week_top_data(request.user.username, 'math')
    lastweek = calc_lastweek_data(request.user.username)
    average = calc_average_data(request.user.username, 'math')
    h_average = calc_average_hour_data(request.user.username, 'math')
    label = calc_getlabel(average)
    if calc_week['nonecount'] == 7:
        top_d[0] = 10

    cont = {'weekdays': week_days, 'calcweek': calc_week, 'topdata': top_d, 'increment': top_d[0]/10, 'lastweek': lastweek, 'average': average, 'h_average': h_average
            , 'label': label}
    return render(request, 'elections/viewstatistics_math.html', cont)

# 과학 통계량 보여주는 view
def statisticsview_science(request):
    week_days = get_weeks_date(0)
    calc_week = calc_week_data(request.user.username)
    top_d = calc_week_top_data(request.user.username, 'science')
    lastweek = calc_lastweek_data(request.user.username)
    average = calc_average_data(request.user.username, 'science')
    h_average = calc_average_hour_data(request.user.username, 'science')
    label = calc_getlabel(average)
    if calc_week['nonecount'] == 7:
        top_d[0] = 10

    cont = {'weekdays': week_days, 'calcweek': calc_week, 'topdata': top_d, 'increment': top_d[0]/10, 'lastweek': lastweek, 'average': average, 'h_average': h_average
            , 'label': label}
    return render(request, 'elections/viewstatistics_science.html', cont)

def statisticsview_korean(request):
    week_days = get_weeks_date(0)
    calc_week = calc_week_data(request.user.username)
    top_d = calc_week_top_data(request.user.username, 'korean')
    lastweek = calc_lastweek_data(request.user.username)
    average = calc_average_data(request.user.username, 'korean')
    h_average = calc_average_hour_data(request.user.username, 'korean')
    label = calc_getlabel(average)
    if calc_week['nonecount'] == 7:
        top_d[0] = 10

    cont = {'weekdays': week_days, 'calcweek': calc_week, 'topdata': top_d, 'increment': top_d[0]/10, 'lastweek': lastweek, 'average': average, 'h_average': h_average
            , 'label': label}
    return render(request, 'elections/viewstatistics_korean.html', cont)

def statisticsview_english(request):
    week_days = get_weeks_date(0)
    calc_week = calc_week_data(request.user.username)
    top_d = calc_week_top_data(request.user.username, 'english')
    lastweek = calc_lastweek_data(request.user.username)
    average = calc_average_data(request.user.username, 'english')
    h_average = calc_average_hour_data(request.user.username, 'english')
    label = calc_getlabel(average)
    if calc_week['nonecount'] == 7:
        top_d[0] = 10

    cont = {'weekdays': week_days, 'calcweek': calc_week, 'topdata': top_d, 'increment': top_d[0]/10, 'lastweek': lastweek, 'average': average, 'h_average': h_average
            , 'label': label}
    return render(request, 'elections/viewstatistics_english.html', cont)

def statisticsview_all(request):
    calc_month = calc_average_month_data(request.user.username)
    return render(request, 'elections/viewstatistics_all.html', {'calcmonth': calc_month})

# ======================================================================================================= #

# 공부기록 업데이트 view
def statisticscalendar(request):
    days = getmonthdays()
    cont = {'days': days, 'today': gettoday(), 'month': getmonth(), 'year': getyear()}
    return render_to_response('elections/statisticscalender.html', cont)

# ======================================================================================================= #

# 입력창에서 받은 값 처리 view
def statisticsform(request):
    form = StatisticsWriteForm(request.POST or None)

    if form.is_valid():
        dm = DBManager()
        query = dm.getusertodaydata(request.user.username)
        math = form.cleaned_data.get('math')
        m_math = form.cleaned_data.get('m_math')

        korean = form.cleaned_data.get('korean')
        m_korean = form.cleaned_data.get('m_korean')

        science = form.cleaned_data.get('science')
        m_science = form.cleaned_data.get('m_science')

        english = form.cleaned_data.get('english')
        m_english = form.cleaned_data.get('m_english')
        #if query exsist is True >> 데이터 수정 , else >> 데이터 생성
        if query.exists():
            query.update(mathhour=calc_study_time(math, m_math), koreanhour=calc_study_time(korean, m_korean), sciencehour=calc_study_time(science, m_science),
                         englishhour=calc_study_time(english, m_english))
            return render(request, 'elections/statistics.html')
        else:
            model_study_data = UserStudyData(date=str_yearnow(),name=request.user.username, mathhour=calc_study_time(math, m_math), koreanhour=calc_study_time(korean, m_korean),
                                  englishhour=calc_study_time(english, m_english), sciencehour=calc_study_time(science, m_science))
            model_study_data.save()
            return render(request, 'elections/statistics.html')

    return render(request, 'elections/statisticsform.html', {'form' : form})

def signup(request):
    form = CreateUserForm(request.POST or None)
    if request.user.is_authenticated:
        return redirect('index')

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        c_password = form.cleaned_data.get('password2')

        existsID = User.objects.filter(username=username).exists()

        if password == c_password and existsID is False:
            form.signup()
        else:
            content = {'form' : form, 'error' : "이미 가입된 아이디 이거나 비밀번호 재확인을 해주세요"}
            content.update(csrf(request))
            return render_to_response('elections/register.html', content)
        return redirect('index')

    return render(request, 'elections/register.html', {'form': form})


def login_view(request):
    form = UserLoginForm(request.POST or None)
    cont = {}
    if request.user.is_authenticated:
        return redirect('index')

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            cont['form'] = form
            cont['error'] = 'Login failed!'
            cont.update(csrf(request))
            return render_to_response('elections/login.html', cont)
    else:
        try:
            username = form.cleaned_data.get('username')
            existsID = User.objects.filter(username=username).exists()

            if existsID is False:
                cont['form'] = form
                cont['error'] = '가입되지 않은 회원입니다!'
                cont.update(csrf(request))
                return render_to_response('elections/login.html', cont)
        except:
            return render(request, 'elections/login.html', {"form": form, "title": 'Login'})

    return render(request, 'elections/login.html', {"form": form, "title": 'Login'})

# ======================================================================================================= #

# Java API 연동 (csrf token)

# Response user all data
# @return dict
@csrf_exempt
def response_user_data(request):
    username = request.POST['username']
    db = DBManager()
    data = db.get_dict_userdata(username=username)

    return JsonResponse(data)

# Response user data filter
# @return dict
@csrf_exempt
def response_user_cond_data(request):
    username = request.POST['username']
    year = request.POST['year']
    month = request.POST['month']
    day = request.POST['day']

    db = DBManager()
    dict_data = db.get_dict_userdata_cond(username, year, month, day)

    return JsonResponse(dict_data)

# Response user id&password registered check
# @return boolean
@csrf_exempt
def response_user_valid(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        return JsonResponse({'valid': True })

    return JsonResponse({'valid': False})

# Response user week statistics
# return dict
@csrf_exempt
def response_user_statistics_week(request):
    username = request.POST['username']

    calcweek = calc_week_data(username=username)
    return JsonResponse(calcweek)

# Response user average month statistics
# return dict
@csrf_exempt
def response_user_statistics_month(request):
    username = request.POST['username']

    calcmonth = calc_average_month_data(username=username)
    return JsonResponse(calcmonth)

