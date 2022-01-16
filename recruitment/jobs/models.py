from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from interview.models import DEGREE_TYPE
# Create your models here.

JobTypes=[
    (0, "Technology"),
    (1, "Product"),
    (2, "Marketing"),
    (3, "Design")
]

Cities = [
    (0, "Helsinki"),
    (1, "Tampere"),
    (2, "Oulu")
]

class Job(models.Model):
    job_type = models.SmallIntegerField(blank=False, choices=JobTypes, verbose_name="Job Classification")
    job_name = models.CharField(max_length=250, blank=False, verbose_name="Job name")
    job_city = models.SmallIntegerField(choices=Cities, blank=False, verbose_name="Basement")
    job_responsibility = models.TextField(max_length=1024, verbose_name="Job Description")
    job_requirement = models.TextField(max_length=1024, blank=False, verbose_name="Job requirement")
    creator = models.ForeignKey(User, verbose_name="Creator", null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(verbose_name="Created Date", default=datetime.now)
    modified_date = models.DateTimeField(verbose_name="Modified Date", default=datetime.now)

    class Meta:
        verbose_name = u'Job',
        verbose_name_plural = u'Jobs'


class Resume(models.Model):
    # Translators: 简历实体的翻译
    username = models.CharField(max_length=135)
    applicant = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    city = models.CharField(max_length=135)
    phone = models.CharField(max_length=135)
    email = models.EmailField(max_length=135, blank=True)
    apply_position = models.CharField(max_length=135, blank=True)
    born_address = models.CharField(max_length=135, blank=True)
    gender = models.CharField(max_length=135, blank=True)

    # 学校与学历信息
    bachelor_school = models.CharField(max_length=135, blank=True)
    master_school = models.CharField(max_length=135, blank=True)
    doctor_school = models.CharField(max_length=135, blank=True)
    major = models.CharField(max_length=135, blank=True)
    degree = models.CharField(max_length=135, choices=DEGREE_TYPE, blank=True)
    created_date = models.DateTimeField(verbose_name="创建日期", default=datetime.now)
    modified_date = models.DateTimeField(verbose_name="修改日期", auto_now=True)

    # 候选人自我介绍，工作经历，项目经历
    candidate_introduction = models.TextField(max_length=1024, blank=True)
    work_experience = models.TextField(max_length=1024, blank=True)
    project_experience = models.TextField(max_length=1024, blank=True)

    class Meta:
        verbose_name = u'Resume'
        verbose_name_plural = u'Resumes'
