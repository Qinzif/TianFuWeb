# _*_ encoding:utf-8 _*_
from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.views.generic import View
from pure_pagination import Paginator,EmptyPage,PageNotAnInteger
from django.http import HttpResponse
from .models import CourseOrg,CityDict,team,pictures,works,task
from .forms import UserOfferForm
from courses.models import CourseOrg,Course
from operation.models import UserFavorite
from django.db.models import Q

# Create your views here.
class OrgView(View):
    def get(self,request):
        all_orgs=CourseOrg.objects.all()
        hot_orgs=all_orgs.order_by("-click_nums")[:3]
        all_citys=CityDict.objects.all()

        search_keywords = request.GET.get('keywords', "")
        if search_keywords:
            all_orgs = all_orgs.filter(
                Q(name__icontains=search_keywords) | Q(desc__icontains=search_keywords))

        #取出筛选城市
        city_id=request.GET.get("city","")
        if city_id:
            all_orgs=all_orgs.filter(city_id=int(city_id))
        #类别筛选
        category=request.GET.get('ct',"")
        if category:
            all_orgs=all_orgs.filter(category=category)
        sort=request.GET.get('sort',"")
        if sort:
            if sort=="students":
                all_orgs=all_orgs.order_by("-students")
            elif sort=="courses":
                all_orgs=all_orgs.order_by("-course_nums")

        #对课程机构进行分页
        org_nums=all_orgs.count()
        try:
            page=request.GET.get('page',1)
        except PageNotAnInteger:
            page=1
        p=Paginator(all_orgs,1,request=request)
        orgs=p.page(page)
        return render(request,"org-list.html",{
            'all_orgs':orgs,
            'all_citys':all_citys,
            'org_nums':org_nums,
            'city_id':city_id,
            'category':category,
            'hot_orgs':hot_orgs,
            'sort':sort,
        })

class AddOfferView(View):
    #用户添加提供信息
    def post(self,request):
        useroffer_form=UserOfferForm(request.POST)
        if useroffer_form.is_valid():
            user_offer=useroffer_form.save(commit=True)
            return HttpResponse('{"status":"success"}',content_type='application/json')
        else:
            return HttpResponse('{"status":"fail","msg":"添加出错"}',content_type='application/json')

class OrgHomeView(View):
    def get(self,request,org_id):
        current_page = "home"
        course_org=CourseOrg.objects.get(id=int(org_id))
        course_org.click_nums+=1
        course_org.save()
        #判断是否收藏
        has_fav=False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user,fav_id=course_org.id,fav_type=2):
                has_fav=True
        all_courses=course_org.course_set.all()[:3]
        return render(request,'org-detail-homepage.html',{
            'all_courses':all_courses,
            'course_org':course_org,
            'current_page': current_page,
            'has_fav':has_fav,
        })

class OrgCourseView(View):
    def get(self,request,org_id):
        current_page="course"
        course_org=CourseOrg.objects.get(id=int(org_id))
        # 判断是否收藏
        has_fav = False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        all_courses=course_org.course_set.all()

        # 对课程机构进行分页
        course_nums = all_courses.count()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_courses, 1, request=request)
        courses = p.page(page)
        return render(request,'org-detail-course.html',{
            'all_courses':courses,
            'course_org':course_org,
            'course_nums':course_nums,
            'current_page':current_page,
            'has_fav': has_fav,
        })

class OrgDescView(View):
    def get(self,request,org_id):
        current_page = "desc"
        course_org=CourseOrg.objects.get(id=int(org_id))
        # 判断是否收藏
        has_fav = False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        return render(request,"org-detail-desc.html",{
            'current_page':current_page,
            'course_org':course_org,
            'has_fav': has_fav,
        })

class AddFavView(View):
    #用户收藏以及取消收藏
    def post(self,request):
        fav_id=request.POST.get('fav_id',0)
        fav_type=request.POST.get('fav_type',0)
        if not request.user.is_authenticated:
            return HttpResponse('{"status":"fail","msg":"用户未登录"}',content_type='application/json')
        exist_records=UserFavorite.objects.filter(user=request.user,fav_id=int(fav_id),fav_type=int(fav_type))
        if exist_records:
            #记录已经存在，表示用户想取消收藏
            exist_records.delete()
            if int(fav_type==1):
                course=Course.objects.get(id=int(fav_id))
                course.fav_nums-=1
                if course.fav_nums<0:
                    course.fav_nums=0
                course.save()
            elif int(fav_type==2):
                course_org=CourseOrg.objects.get(id=int(fav_id))
                course_org.fav_nums-=1
                if course_org.fav_nums<0:
                    course_org.fav_nums=0
                course_org.save()
            elif int(fav_type==3):
                teamm=team.objects.get(id=int(fav_id))
                teamm.fav_nums-=1
                if teamm.fav_nums<0:
                    teamm.fav_nums=0
                teamm.save()
            return HttpResponse('{"status":"success","msg":"收藏"}',content_type='application/json')
        else:
            user_fav=UserFavorite()
            if int(fav_id)>0 and int(fav_type)>0:
                user_fav.user=request.user
                user_fav.fav_id=int(fav_id)
                user_fav.fav_type=int(fav_type)
                user_fav.save()
                if int(fav_type == 1):
                    course = Course.objects.get(id=int(fav_id))
                    course.fav_nums += 1
                    course.save()
                elif int(fav_type == 2):
                    course_org = CourseOrg.objects.get(id=int(fav_id))
                    course_org.fav_nums += 1
                    course_org.save()
                elif int(fav_type == 3):
                    teamm = team.objects.get(id=int(fav_id))
                    teamm.fav_nums += 1
                    teamm.save()
                return HttpResponse('{"status":"fail","msg":"已收藏"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"fail","msg":"收藏出错"}', content_type='application/json')

#天釜在线列表页
class TeamListView(View):
    def get(self,request):
        all_teams=team.objects.all()
        team_nums = all_teams.count()

        search_keywords = request.GET.get('keywords', "")
        if search_keywords:
            all_teams = all_teams.filter(
                Q(name__icontains=search_keywords) | Q(points__icontains=search_keywords))

        sort = request.GET.get('sort', "")
        if sort:
            if sort == "hot":
                all_teams = all_teams.order_by("-click_nums")
        return render(request,"teachers-list.html",{
            'all_teams':all_teams,
            'team_nums':team_nums,
            'sort':sort,
        })

class TeamDetailView(View):
    def get(self,request,team_id):
        teams=team.objects.get(id=int(team_id))
        teams.click_nums+=1
        teams.save()
        all_pictures=pictures.objects.filter(forteam=teams)
        has_team_faved=False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user,fav_type=3,fav_id=teams.id):
                has_team_faved=True
        return render(request,"teacher-detail.html",{
            'teams':teams,
            'all_pictures':all_pictures,
            'has_team_faved':has_team_faved,
        })

class WorkListView(View):
    def get(self,request):
        all_works=works.objects.all()
        work_nums=all_works.count()

        search_keywords = request.GET.get('keywords', "")
        if search_keywords:
            all_works = all_works.filter(
                Q(title__icontains=search_keywords)| Q(author__icontains=search_keywords) | Q(points__icontains=search_keywords))

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_works, 3, request=request)
        workss = p.page(page)
        return render(request,"works-list.html",{
            'all_works':workss,
            'work_nums':work_nums,
        })

class TaskView(View):
    def get(self,request):
        all_tasks=task.objects.all()
        count=all_tasks.count()
        return render(request,"task.html",{
            'all_tasks':all_tasks,
            'count':count,
        })


