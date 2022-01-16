from django.conf.urls import url
from jobs import views
from django.urls import path

urlpatterns = [
    # Joblist
    url(r"^joblist/", views.joblist, name="joblist"),

    # Jobinfo
    url(r"^job/(?P<job_id>\d+)/$", views.detail, name="detail"),

    # Apply Page
    path('resume/add/', views.ResumeCreateView.as_view(), name='resume_add'),

    # Home Page
    url(r'^$', views.joblist, name="name"),


]