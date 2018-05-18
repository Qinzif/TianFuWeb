# _*_ encoding:utf-8 _*_
import xadmin
from .models import CityDict,CourseOrg,team,pictures,works,workpics,task

class CityDictAdmin(object):
    list_display=['name','desc','add_time']
    search_fields=['name','desc']
    list_filter=['name','desc','add_time']

class CourseOrgAdmin(object):
    list_display=['name','desc','tag','category','click_nums','fav_nums','image','address','city','students','course_nums','add_time']
    search_fields=['name','desc','tag','category','click_nums','fav_nums','image','address','city','students','course_nums']
    list_filter=['name','desc','tag','category','click_nums','fav_nums','image','address','city','students','course_nums','add_time']
    style_fields = {'desc': "ueditor",}

class teamAdmin(object):
    list_display=['name','found_years','work_department','location','principal1','mobile1','principal2','mobile2','stu_nums','group','points','click_nums','fav_nums','image','add_time']
    search_fields=['name','found_years','work_department','location','principal1','mobile1','principal2','mobile2','stu_nums','group','points','click_nums','fav_nums','image']
    list_filter=['name','found_years','work_department','location','principal1','mobile1','principal2','mobile2','stu_nums','group','points','click_nums','fav_nums','image','add_time']
    style_fields = {'group': "ueditor",'points': "ueditor",}

class picturesAdmin(object):
    list_display=['title','image', 'forteam', 'add_time']
    search_fields=['title', 'image', 'forteam']
    list_filter=['title','image','forteam','add_time']

class worksAdmin(object):
    list_display = ['title','author','points','add_time']
    search_fields =['title','author','points']
    list_filter = ['title','author','points','add_time']
    style_fields = {'points': "ueditor"}

class workpicsAdmin(object):
    list_display = ['title','image','forwork','add_time']
    search_fields =['title','image','forwork']
    list_filter = ['title','image','forwork','add_time']

class taskAdmin(object):
    list_display = ['theme','organizer','require','plan','url','download','add_time']
    search_fields =['theme','organizer','require','plan','download','url']
    list_filter = ['theme','organizer','require','plan','url','download','add_time']
    style_fields = {'require': "ueditor",'plan': "ueditor"}

xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(team,teamAdmin)
xadmin.site.register(pictures,picturesAdmin)
xadmin.site.register(works,worksAdmin)
xadmin.site.register(workpics,workpicsAdmin)
xadmin.site.register(task,taskAdmin)