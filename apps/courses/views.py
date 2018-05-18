from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from pure_pagination import Paginator,EmptyPage,PageNotAnInteger
from django.http import HttpResponse
from .models import Course,CourseResource,Lesson,Video
from operation.models import UserFavorite,CourseComments,UserCourse
from utils.mixin_utils import LoginRequiredMixin
from django.db.models import Q

class CourseListView(View):
    def get(self,request):
        all_courses=Course.objects.all().order_by("-add_time")
        hot_courses=Course.objects.all().order_by("-click_nums")

        search_keywords=request.GET.get('keywords',"")
        if search_keywords:
            all_courses=all_courses.filter(Q(name__icontains=search_keywords)|Q(desc__icontains=search_keywords)|Q(detail__icontains=search_keywords))

        #课程排序
        sort=request.GET.get('sort',"")
        if sort:
            if sort=="students":
                all_courses=all_courses.order_by("-students")
            elif sort=="hot":
                all_courses=all_courses.order_by("-click_nums")[:3]
        # 对课程机构进行分页
        course_nums = all_courses.count()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_courses, 1, request=request)
        courses = p.page(page)
        return render(request,"course-list.html",{
            'all_courses':courses,
            'course_nums':course_nums,
            'sort':sort,
            'hot_courses':hot_courses,
        })

class CourseDetailView(View):
    def get(self,request,course_id):
        course=Course.objects.get(id=int(course_id))
        #增加课程点击数
        course.click_nums+=1
        course.save()

        has_fav_course=False
        has_fav_org=False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user,fav_id=course.id,fav_type=1):
                has_fav_course=True
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user,fav_id=course.course_org.id,fav_type=2):
                has_fav_org=True

        tag=course.tag
        if tag:
            relate_courses=Course.objects.filter(tag=tag)[:2]
        else:
            relate_courses=[]
        return render(request,"course-detail.html",{
            'course':course,
            'relate_courses':relate_courses,
            'has_fav_course':has_fav_course,
            'has_fav_org':has_fav_org,
        })

class CourseVideoView(LoginRequiredMixin,View):
    def get(self,request,course_id):
        course=Course.objects.get(id=int(course_id))
        course.students+=1
        course.save()
        #查询用户已经关联了该课程
        user_courses=UserCourse.objects.filter(user=request.user,course=course)
        if not user_courses:
            user_course=UserCourse(user=request.user,course=course)
            user_course.save()
        user_courses = UserCourse.objects.filter(course=course)
        user_ids = [user_course.user_id for user_course in user_courses]
        all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)
        # 取出所有课程id
        course_ids = [user_course.course_id for user_course in all_user_courses]
        # 获取学过该课程的同学所学的课程
        relates_cources = Course.objects.filter(id__in=course_ids).order_by("-click_nums")[:5]
        all_resources=CourseResource.objects.filter(course=course)
        all_lessons=Lesson.objects.filter(course=course).order_by("add_time")
        # 对章节信息进行分页
        lesson_nums = all_lessons.count()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_lessons, 4, request=request)
        lessons = p.page(page)
        return render(request,"course-video.html",{
            'course':course,
            'course_resources':all_resources,
            'all_lessons':lessons,
            'lesson_nums':lesson_nums,
            'relates_cources': relates_cources,
        })

class CourseCommentView(LoginRequiredMixin,View):
    def get(self,request,course_id):
        course=Course.objects.get(id=int(course_id))
        user_courses=UserCourse.objects.filter(course=course)
        user_ids=[user_course.user.id for user_course in user_courses]
        all_user_courses=Course.objects.filter(id__in=user_ids)
        #取出所有课程id
        course_ids=[user_course.course.id for user_course in user_courses]
        #获取学过该课程的同学所学的课程
        relates_cources=Course.objects.filter(id__in=course_ids).order_by("-click_nums")[:5]
        all_resources=CourseResource.objects.filter(course=course)
        all_comments=CourseComments.objects.all()
        # 对章节信息进行分页
        commnet_nums = all_comments.count()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_comments, 1, request=request)
        comments = p.page(page)
        return render(request,"course-comment.html",{
            'course':course,
            'course_resources':all_resources,
            'commnet_nums':commnet_nums,
            'all_comments':comments,
            'relates_cources':relates_cources,
        })

class AddComments(View):
    #用户添加课程评论
    def post(self,request):
        if not request.user.is_authenticated:
            return HttpResponse('{"status":"fail","msg":"用户未登录"}', content_type='application/json')
        course_id= request.POST.get("course_id",0)
        comments=request.POST.get("comments","")
        if int(course_id)>0 and comments:
            course_comments=CourseComments()
            course=Course.objects.get(id=int(course_id))
            course_comments.course=course
            course_comments.comments=comments
            course_comments.user=request.user
            course_comments.save()
            return HttpResponse('{"status":"success","msg":"添加成功"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail","msg":"添加失败"}', content_type='application/json')

class CourseVideoPlayView(LoginRequiredMixin,View):
    #视频播放页面
    def get(self,request,video_id):
        video=Video.objects.get(id=int(video_id))
        course=video.lesson.course
        course.students+=1
        course.save()
        #查询用户已经关联了该课程
        user_courses=UserCourse.objects.filter(user=request.user,course=course)
        if not user_courses:
            user_course=UserCourse(user=request.user,course=course)
            user_course.save()
        user_courses = UserCourse.objects.filter(course=course)
        user_ids = [user_course.user_id for user_course in user_courses]
        all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)
        # 取出所有课程id
        course_ids = [user_course.course_id for user_course in all_user_courses]
        # 获取学过该课程的同学所学的课程
        relates_cources = Course.objects.filter(id__in=course_ids).order_by("-click_nums")[:5]
        all_resources=CourseResource.objects.filter(course=course)
        all_lessons=Lesson.objects.filter(course=course).order_by("add_time")
        # 对章节信息进行分页
        lesson_nums = all_lessons.count()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_lessons, 4, request=request)
        lessons = p.page(page)
        return render(request,"course-play.html",{
            'course':course,
            'course_resources':all_resources,
            'all_lessons':lessons,
            'lesson_nums':lesson_nums,
            'relates_cources': relates_cources,
            'video':video,
        })