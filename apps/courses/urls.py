# _*_ encoding:utf-8 _*_
from django.conf.urls import url,include
from .views import CourseListView,CourseDetailView,CourseVideoView,CourseCommentView,AddComments,CourseVideoPlayView

urlpatterns = [
    url(r'^list/$',CourseListView.as_view(),name='list'),
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="detail"),
    url(r'^video/(?P<course_id>\d+)/$', CourseVideoView.as_view(), name="video"),
    url(r'^comment/(?P<course_id>\d+)/$', CourseCommentView.as_view(), name="comment"),
    url(r'^add_comment/$', AddComments.as_view(), name="comment"),
    url(r'^video_play/(?P<video_id>\d+)/$', CourseVideoPlayView.as_view(), name="video_play"),

]