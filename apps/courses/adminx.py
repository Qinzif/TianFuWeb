# _*_ encoding:utf-8 _*_
import xadmin
from .models import Course,Lesson,Video,CourseResource


class CourseAdmin(object):
    list_display=['course_org','name','desc','detail','is_banner','teacher','degree','learn_times','students','fav_nums','image','click_nums','category','tag','add_time','youneed_know','teacher_tell']
    search_fields=['course_org','name','desc','detail','is_banner','teacher','degree','learn_times','students','fav_nums','image','click_nums','category','tag','youneed_know','teacher_tell']
    list_filter=['course_org','name','desc','detail','is_banner','teacher','degree','learn_times','students','fav_nums','image','click_nums','category','tag','add_time','youneed_know','teacher_tell']
    style_fields={"detail":"ueditor"}


class LessonAdmin(object):
    list_display =['course','name','add_time']
    search_fields =['course','name']
    list_filter =['course','name','add_time']


class VideoAdmin(object):
    list_display =['lesson','name','learn_times','url','add_time']
    search_fields =['lesson','name','learn_times','url']
    list_filter =['lesson','name','learn_times','url','add_time']


class CourseResourceAdmin(object):
    list_display =['course','name','download','add_time']
    search_fields =['course','name','download']
    list_filter =['course','name','download','add_time']


xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)

