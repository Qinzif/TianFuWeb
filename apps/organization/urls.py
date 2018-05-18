#_*_ encoding:utf-8 _*_
from django.conf.urls import url,include
from .views import OrgView,AddOfferView,OrgHomeView,OrgCourseView,OrgDescView,AddFavView,TeamListView,TeamDetailView,WorkListView,TaskView

urlpatterns =[
    url(r'^list/$', OrgView.as_view(), name="org_list"),
    url(r'^add_offer/$',AddOfferView.as_view(),name="add_offer"),
    url(r'^home/(?P<org_id>\d+)/$',OrgHomeView.as_view(),name="home"),
    url(r'^course/(?P<org_id>\d+)/$', OrgCourseView.as_view(), name="course"),
    url(r'^desc/(?P<org_id>\d+)/$', OrgDescView.as_view(), name="desc"),
    #课程收藏
    url(r'^add_fav/$', AddFavView.as_view(), name="add_fav"),
    #团队列表页
    url(r'^team/list/$', TeamListView.as_view(), name="team_list"),
    url(r'^team/detail/(?P<team_id>\d+)/$', TeamDetailView.as_view(), name="team_detail"),
    url(r'^works/list/$', WorkListView.as_view(), name="works"),
    url(r'^task/$', TaskView.as_view(), name="task"),

]