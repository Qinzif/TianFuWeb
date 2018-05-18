# _*_ encoding:utf-8 _*_

from django.conf.urls import url,include
from .views import UserinfoView, UploadImageView,UpdatePwdView,SendemailCodeView,UpdateEmailView
from .views import MyCourseView,MyFavOrgView,MyFavTeamView,MyFavCourseView,MessageView
from .models import UserProfile

urlpatterns = [
    url(r'^info/$',UserinfoView.as_view(),name="info"),
    url(r'^image/upload/$', UploadImageView.as_view(), name="info"),
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name="update_pwd"),
    url(r'^sendemail_code/$', SendemailCodeView.as_view(), name="sendemail_code"),
    url(r'^update_email/$', UpdateEmailView.as_view(), name="update_email"),
    url(r'^mycourse/$', MyCourseView.as_view(), name="mycourse"),
    url(r'^myfav/org/$', MyFavOrgView.as_view(), name="myfav_org"),
    url(r'^myfav/team/$', MyFavTeamView.as_view(), name="myfav_team"),
    url(r'^myfav/course/$', MyFavCourseView.as_view(), name="myfav_course"),
    url(r'^message/$', MessageView.as_view(), name="message"),

]