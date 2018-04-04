import datetime

#해당 달의 날짜를 배열의 형태로 반환함
def getmonthdays():
    time = datetime.datetime.now()
    lastday = getlastday(time.year, time.month)

    cont = []
    for i in range(1, lastday+1):
        cont.append(i)
    return cont

def getlastday(year, month):
    time = datetime.date(year, month, 1)
    lastday = -1
    if time.month % 2 == 1:
        lastday = 31
    elif time.month % 2 == 0:
        lastday = 30
    elif time.month == 2:
        lastday = leap_day(time.year)
    return lastday

def getnow():
    return datetime.datetime.now()

#현재 날짜 반환
def gettoday():
    return datetime.datetime.now().day

def getmonth():
    return datetime.datetime.now().month

def getyear():
    return datetime.datetime.now().year

#윤달 계산 함수
def leap_day(year):
    if year % 4 == 0 and year % 100 != 0 and year % 400 == 0:
        return 29
    else:
        return 28

def strnow():
    time = datetime.datetime.now()
    month = time.month
    day = time.day
    return str(month) + "-" + str(day)

def str_yearnow():
    time = datetime.datetime.now()
    return str(time.year) + "-" + str(time.month) + "-" + str(time.day)

# 주차 계산을 위한 주 구하기
def get_weeks():
    dt = datetime.datetime.now()
    return dt.isocalendar()[1]-1

def get_weeks_date(n_week):
    gswd = get_start_week_day(n_week)
    list = {}
    for i in range(0, 7):
        n_date = add_days(i, gswd)
        list[i] = str(n_date.month) + "월" + str(n_date.day) + "일"
    return list

# 주의 시작일 구하기 (월요일)
def get_start_week_day(n_week):
    week = get_weeks()
    date = datetime.date(datetime.datetime.now().year, 1, 1)
    return date + datetime.timedelta(weeks=week-n_week)

def add_days(add_time, date):
    return date + datetime.timedelta(days=add_time)

def fdstr(date):
    return str(date.year) + "-" + str(date.month) + "-" + str(date.day)

def m_date(year, month, day):
    return datetime.date(year, month, day)