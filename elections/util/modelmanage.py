from elections.models import UserStudyData
from django.utils.timezone import now
from elections.util.time import strnow, str_yearnow, fdstr
from datetime import date

#DB managing class
class DBManager:

    #유저의 모든 데이터 쿼리셋 반환
    def getuserdatas(self, username):
        return UserStudyData.objects.filter(name=username)

    #유저가 오늘 업데이트한 데이터 쿼리셋을 반환함
    def getusertodaydata(self, username):
        return UserStudyData.objects.filter(name=username, date=str_yearnow())

    #유저 데이터 검색 쿼리셋 반환
    def getcond_data(self, date, username):
        return UserStudyData.objects.filter(name=username, date=date)

    # 유저 데이터 딕셔너리 반환
    def get_dict_userdata (self, username):
        query = self.getuserdatas(username=username)

        data = {}
        number = 0

        if query.exists():
            for q_index in query:
                data[number] = {'math': q_index.mathhour, 'science': q_index.sciencehour, 'english': q_index.englishhour, 'korean': q_index.koreanhour}
                number+=1
        return data

    # User cond data 딕셔너리 반환
    def get_dict_userdata_cond(self, username, year, month, day):
        d = date(int(year), int(month), int(day))
        date_str = fdstr(d)
        query = self.getcond_data(date=date_str, username=username)
        list = {}

        if query.exists():
            for q_index in query:
                list['math'] = q_index.mathhour
                list['english'] = q_index.englishhour
                list['science'] = q_index.sciencehour
                list['korean'] = q_index.koreanhour

        return {date_str: list}