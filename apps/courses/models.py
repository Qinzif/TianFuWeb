# _*_ encoding:utf-8 _*_

from datetime import datetime
from django.db import models
from organization.models import CourseOrg
from DjangoUeditor.models import UEditorField

# Create your models here.


class Course(models.Model):
    course_org=models.ForeignKey(CourseOrg,verbose_name=u'课程机构',null=True,blank=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,verbose_name=u'课程名')
    desc=models.CharField(max_length=300,verbose_name=u'课程描述')
    detail=UEditorField(verbose_name=u"课程详情", imagePath="course/ueditor/", width=1000, height=300,
                        filePath="course/ueditor/", default='')
    is_banner=models.BooleanField(default=False,verbose_name=u'是否轮播')
    teacher=models.CharField(max_length=50,default=u'',verbose_name=u'讲师',null=True,blank=True)
    degree=models.CharField(choices=(('cj',u'初级'),('zj',u'中级'),('gj',u'高级')),max_length=2)
    learn_times=models.IntegerField(default=0,verbose_name=u'学习时长(分钟数)')
    students=models.IntegerField(default=0,verbose_name=u'学习人数')
    fav_nums=models.IntegerField(default=0,verbose_name=u'收藏人数')
    image=models.ImageField(upload_to='courses/%Y/%m',verbose_name=u'封面图',max_length=100)
    click_nums=models.IntegerField(default=0,verbose_name=u'点击数')
    category=models.CharField(default=u'媒体',max_length=20,verbose_name=u'课程类别')
    tag=models.CharField(default='',verbose_name=u'课程标签',max_length=10)
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')
    youneed_know=models.CharField(default='',max_length=300,verbose_name=u'课程须知')
    teacher_tell=models.CharField(default='',max_length=300,verbose_name=u'老师告诉')

    class Meta:
        verbose_name=u'课程'
        verbose_name_plural=verbose_name

    def get_zj_nums(self):
        # 获取课程章节数
        return self.lesson_set.all().count()

    def get_learn_users(self):
        return self.usercourse_set.all()[:5]

    def get_course_lesson(self):
        return self.lesson_set.all()

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course=models.ForeignKey(Course,verbose_name=u'课程',on_delete=models.CASCADE)
    name=models.CharField(max_length=100,verbose_name=u'章节名')
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name=u'章节'
        verbose_name_plural=verbose_name

    def get_lesson_video(self):
        return self.video_set.all()

    def __str__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u'章节', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u'视频名')
    learn_times = models.IntegerField(default=0, verbose_name=u'学习时长(分钟数)')
    url = models.CharField(default='', max_length=200, verbose_name=u'访问地址')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'视频'
        verbose_name_plural = verbose_name

        def __str__(self):
            return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u'课程', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u'名称')
    download = models.FileField(upload_to='course/resource/%Y/%m', verbose_name=u'资源文件', max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程资源'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name