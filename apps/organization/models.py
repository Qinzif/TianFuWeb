# _*_ encoding:utf-8 _*_
from django.db import models
from datetime import datetime
from DjangoUeditor.models import UEditorField

# Create your models here.

class CityDict(models.Model):
	name =models.CharField(max_length=20,verbose_name=u'课程分类')
	desc=models.CharField(max_length=200,verbose_name=u'描述')
	add_time=models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

	class Meta:
		verbose_name=u'课程分类'
		verbose_name_plural=verbose_name

	def __str__(self):
		return self.name

class CourseOrg(models.Model):
	name=models.CharField(max_length=50,verbose_name=u'机构名称')
	desc=UEditorField(verbose_name=u'机构描述', imagePath="desc/ueditor/", width=1000, height=300,filePath="desc/ueditor/", default='')
	tag=models.CharField(default="权威课程",max_length=30,verbose_name=u'课程类型描述')
	category=models.CharField(default='pxjg',verbose_name=u'机构类别',max_length=20,choices=(('pxjg','培训机构'),('gr','个人'),('gx','高校')))
	click_nums=models.IntegerField(default=0,verbose_name=u'点击数')
	fav_nums=models.IntegerField(default=0,verbose_name=u'收藏数')
	image=models.ImageField(upload_to='org/%Y/%m',verbose_name=u'logo',max_length=100)
	address=models.CharField(max_length=150,verbose_name=u'机构地址')
	city=models.ForeignKey(CityDict,verbose_name=u'课程类别',on_delete=models.CASCADE)
	students=models.IntegerField(default=0,verbose_name=u'学习人数')
	course_nums=models.IntegerField(default=0,verbose_name=u'课程数')
	add_time=models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

	class Meta:
		verbose_name=u'课程机构'
		verbose_name_plural=verbose_name

	def __str__(self):
		return self.name

class team(models.Model):
	name=models.CharField(max_length=20,verbose_name=u'团队名称')
	found_years=models.IntegerField(default=0,verbose_name=u'成立年限')
	work_department=models.CharField(default="数字媒体学院",max_length=50,verbose_name=u'所属院系')
	location=models.CharField(default="",max_length=50,verbose_name=u'团队地址')
	principal1=models.CharField(default="",max_length=20,verbose_name=u'团队负责人1')
	mobile1 = models.CharField(max_length=11, null=True, blank=True,verbose_name=u'负责人1联系电话')
	principal2 = models.CharField(default="",max_length=20, verbose_name=u'团队负责人2')
	mobile2 = models.CharField(max_length=11, null=True, blank=True, verbose_name=u'负责人2联系电话')
	stu_nums=models.IntegerField(default=0,verbose_name=u'团队规模')
	group=UEditorField(verbose_name=u'团队分组', imagePath="group/ueditor/", width=1000, height=300,filePath="group/ueditor/", default='')
	points=UEditorField(verbose_name=u'团队简介', imagePath="points/ueditor/", width=1000, height=300,filePath="points/ueditor/", default='')
	click_nums=models.IntegerField(default=0, verbose_name=u'点击数')
	fav_nums=models.IntegerField(default=0, verbose_name=u'收藏数')
	image=models.ImageField(default='',upload_to='teacher/%Y/%m',verbose_name=u'头像',max_length=100)
	add_time=models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

	class Meta:
		verbose_name=u'团队'
		verbose_name_plural=verbose_name

	def __str__(self):
		return self.name

class pictures(models.Model):
	title=models.CharField(max_length=100,verbose_name=u'标题')
	image=models.ImageField(upload_to='banner/%Y/%m',verbose_name=u'工作室照片',max_length=100)
	forteam=models.ForeignKey(team,verbose_name=u'所在团队',default=u'',on_delete=models.CASCADE)
	add_time=models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

	class Meta:
		verbose_name=u'照片'
		verbose_name_plural=verbose_name

	def __str__(self):
		return self.title

class works(models.Model):
	title=models.CharField(max_length=100,verbose_name=u'作品名称')
	author=models.CharField(max_length=50,verbose_name=u'作者')
	points = UEditorField(verbose_name=u"作品简介", imagePath="point/ueditor/", width=1000, height=300,filePath="point/ueditor/", default='')
	add_time=models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

	class Meta:
		verbose_name=u'作品'
		verbose_name_plural=verbose_name

	def get_works_workpics(self):
		return self.workpics_set.all()

	def __str__(self):
		return self.title

class workpics(models.Model):
	title=models.CharField(max_length=100,verbose_name=u'标题')
	image=models.ImageField(upload_to='banner/%Y/%m',verbose_name=u'作品照片',max_length=100)
	forwork=models.ForeignKey(works,verbose_name=u'所属作品',default=u'',on_delete=models.CASCADE)
	add_time=models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

	class Meta:
		verbose_name=u'作品照片'
		verbose_name_plural=verbose_name

	def __str__(self):
		return self.title

class task(models.Model):
	theme=models.CharField(default='',max_length=50,verbose_name=u'活动主题')
	organizer=models.CharField(default='',max_length=50,verbose_name=u'组织机构')
	require=UEditorField(verbose_name=u"作品要求", imagePath="require/ueditor/", width=1000, height=300,filePath="require/ueditor/", default='')
	plan=UEditorField(verbose_name=u"时间安排", imagePath="plan/ueditor/", width=1000, height=300,filePath="plan/ueditor/", default='')
	url=models.CharField(default='',max_length=50,verbose_name=u'活动官网')
	download=models.FileField(upload_to='org/resource/%Y/%m',verbose_name=u'参赛详情',max_length=100)
	add_time=models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

	class Meta:
		verbose_name=u'任务发布'
		verbose_name_plural=verbose_name

	def __str__(self):
		return self.theme
