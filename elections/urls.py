from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout
from django.conf.urls import include

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^join/$', views.signup, name = 'join'),
    url(r'^statistics/$', views.statistics, name = 'statistics'),
    url(r'^statistics/calendar/$', views.statisticscalendar, name='statisticscalendar'),
    url(r'^statistics/form/$', views.statisticsform, name='statisticsform'),
    url(r'^statistics/view/math/$', views.statisticsview_math, name='statisticsview_math'),
    url(r'^statistics/view/science/$', views.statisticsview_science, name='statisticsview_science'),
    url(r'^statistics/view/korean/$', views.statisticsview_korean, name='statisticsview_korean'),
    url(r'^statistics/view/english/$', views.statisticsview_english, name='statisticsview_english'),
    url(r'^statistics/view/all/$', views.statisticsview_all, name='statisticsview_all'),

    url(r'^response/userdata', views.response_user_data),
    url(r'^response/userdatedata', views.response_user_cond_data),
    url(r'^response/uservalid', views.response_user_valid),
    url(r'^response/userweekdata', views.response_user_statistics_week),
    url(r'^response/useraveragemonth', views.response_user_statistics_month)


]