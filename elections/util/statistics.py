from datetime import date
from .modelmanage import DBManager
from .time import get_start_week_day, fdstr, add_days, getmonth, getlastday, getyear

# 통계 계산 py
# 1주일 ,1달 단위로 나눠서 통계를 내는 알고리즘
# 1주일 평균 A과목 공부량 = N
# 1달 평균 A과목 공부량 = B
# 저번주랑 이번주 공부량 비교 통계
# 이번달 평균 공부량 통계
# 주/달 최대값 구하는 함수

#총 공부량 분으로 환산
def calc_study_time(hour, minute):
    hour *= 60
    return hour + minute

#주별 데이터 환산
def calc_week_data(username):
    db = DBManager()
    data = {}
    date = get_start_week_day(0)
    nonecount = 0
    for i in range(0, 7):
        n_date = add_days(i, date)
        query = db.getcond_data(fdstr(n_date), username)
        if query.exists():
            for queryindex in query:
                list = {"math": queryindex.mathhour, "korean": queryindex.koreanhour, "english": queryindex.englishhour, "science": queryindex.sciencehour}
                data[i] = list
        else:
            data[i] = {'math': 0, 'korean': 0, 'english': 0, 'science': 0}
            nonecount += 1

    data['nonecount'] = nonecount
    return data

def calc_lastweek_data(username):
    db = DBManager()
    data = {}
    date = get_start_week_day(-1)
    for i in range(0, 7):
        n_date = add_days(i, date)
        query = db.getcond_data(fdstr(n_date), username)
        if query.exists():
            for queryindex in query:
                list = {"math": queryindex.mathhour, "korean": queryindex.koreanhour, "english": queryindex.englishhour, "science": queryindex.sciencehour}
                data[i] = list
        else:
            data[i] = {'math': 0, 'korean': 0, 'english': 0, 'science': 0}

    return data

# 주별 최대 데이터 환산
def calc_week_top_data(username, type):
    data = calc_week_data(username)
    calc_data = []

    for cont in data.keys():

        if cont is not "nonecount":
            v_cont = data[cont]
            calc_data.append(v_cont[type])

    calc_data.sort(reverse=True)
    print(calc_data)

    return calc_data

# 주별 공부시간(분) 환산
def calc_average_data(username, type):
    data = calc_week_data(username)
    all = 0
    for cont in data.keys():

        if cont is not "nonecount":
            v_cont = data[cont]
            all += v_cont[type]

    return round(all/7, 1)

# 주별 공부시간(시) 환산
def calc_average_hour_data(username, type):
    average = calc_average_data(username, type)
    hour = int(average/60)
    minute = round(average%60, 1)
    return str(hour) + "시간" + str(minute) + "분"

# 공부량 label 환산
def calc_getlabel(average):
    hour = int(average/60)
    if hour == 0 or hour <= 5:
        return 0
    elif hour > 5 or hour <= 10:
        return 1
    elif hour > 10:
        return 2

# 지난달 평균 공부시간 환산
def calc_average_month_data(username):
    db = DBManager()

    bmonth = getmonth()-1
    l_month_day = getlastday(getyear(), bmonth)

    math = 0
    korean = 0
    science = 0
    english = 0

    for day in range(1, l_month_day+1):
        fdate = date(getyear(), bmonth, day)
        fdate_str = fdstr(fdate)

        query = db.getcond_data(fdate_str, username)

        if query.exists():
            for q_index in query:
                math += q_index.mathhour
                korean += q_index.koreanhour
                science += q_index.sciencehour
                english += q_index.englishhour

    math /= l_month_day
    korean /= l_month_day
    science /= l_month_day
    english /= l_month_day

    print({'math': round(math,1), 'korean': round(korean, 1), 'science': round(science, 1), 'english': round(english, 1)})
    return {'math': round(math,1), 'korean': round(korean, 1), 'science': round(science, 1), 'english': round(english, 1)}


