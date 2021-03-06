# Generated by Django 2.0.4 on 2018-05-02 16:17

import DjangoUeditor.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityDict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='课程分类')),
                ('desc', models.CharField(max_length=200, verbose_name='描述')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '课程分类',
                'verbose_name_plural': '课程分类',
            },
        ),
        migrations.CreateModel(
            name='CourseOrg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='机构名称')),
                ('desc', DjangoUeditor.models.UEditorField(default='', verbose_name='机构描述')),
                ('tag', models.CharField(default='权威课程', max_length=30, verbose_name='课程类型描述')),
                ('category', models.CharField(choices=[('pxjg', '培训机构'), ('gr', '个人'), ('gx', '高校')], default='pxjg', max_length=20, verbose_name='机构类别')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击数')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏数')),
                ('image', models.ImageField(upload_to='org/%Y/%m', verbose_name='logo')),
                ('address', models.CharField(max_length=150, verbose_name='机构地址')),
                ('students', models.IntegerField(default=0, verbose_name='学习人数')),
                ('course_nums', models.IntegerField(default=0, verbose_name='课程数')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.CityDict', verbose_name='课程类别')),
            ],
            options={
                'verbose_name': '课程机构',
                'verbose_name_plural': '课程机构',
            },
        ),
        migrations.CreateModel(
            name='pictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('image', models.ImageField(upload_to='banner/%Y/%m', verbose_name='工作室照片')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '照片',
                'verbose_name_plural': '照片',
            },
        ),
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(default='', max_length=50, verbose_name='活动主题')),
                ('organizer', models.CharField(default='', max_length=50, verbose_name='组织机构')),
                ('require', DjangoUeditor.models.UEditorField(default='', verbose_name='作品要求')),
                ('plan', DjangoUeditor.models.UEditorField(default='', verbose_name='时间安排')),
                ('url', models.CharField(default='', max_length=50, verbose_name='活动官网')),
                ('download', models.FileField(upload_to='org/resource/%Y/%m', verbose_name='参赛详情')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '任务发布',
                'verbose_name_plural': '任务发布',
            },
        ),
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='团队名称')),
                ('found_years', models.IntegerField(default=0, verbose_name='成立年限')),
                ('work_department', models.CharField(default='数字媒体学院', max_length=50, verbose_name='所属院系')),
                ('location', models.CharField(default='', max_length=50, verbose_name='团队地址')),
                ('principal1', models.CharField(default='', max_length=20, verbose_name='团队负责人1')),
                ('mobile1', models.CharField(blank=True, max_length=11, null=True, verbose_name='负责人1联系电话')),
                ('principal2', models.CharField(default='', max_length=20, verbose_name='团队负责人2')),
                ('mobile2', models.CharField(blank=True, max_length=11, null=True, verbose_name='负责人2联系电话')),
                ('stu_nums', models.IntegerField(default=0, verbose_name='团队规模')),
                ('group', DjangoUeditor.models.UEditorField(default='', verbose_name='团队分组')),
                ('points', DjangoUeditor.models.UEditorField(default='', verbose_name='团队简介')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击数')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏数')),
                ('image', models.ImageField(default='', upload_to='teacher/%Y/%m', verbose_name='头像')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '团队',
                'verbose_name_plural': '团队',
            },
        ),
        migrations.CreateModel(
            name='workpics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('image', models.ImageField(upload_to='banner/%Y/%m', verbose_name='作品照片')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '作品照片',
                'verbose_name_plural': '作品照片',
            },
        ),
        migrations.CreateModel(
            name='works',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='作品名称')),
                ('author', models.CharField(max_length=50, verbose_name='作者')),
                ('points', DjangoUeditor.models.UEditorField(default='', verbose_name='作品简介')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '作品',
                'verbose_name_plural': '作品',
            },
        ),
        migrations.AddField(
            model_name='workpics',
            name='forwork',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='organization.works', verbose_name='所属作品'),
        ),
        migrations.AddField(
            model_name='pictures',
            name='forteam',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='organization.team', verbose_name='所在团队'),
        ),
    ]
