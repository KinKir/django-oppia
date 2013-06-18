# oppia/urls.py
from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView
from oppia.api.resources import *
from tastypie.api import Api

v1_api = Api(api_name='v1')
v1_api.register(TrackerResource())
v1_api.register(CourseResource())
v1_api.register(ScheduleResource())
v1_api.register(TagResource())
v1_api.register(ScorecardResource())
v1_api.register(PointsResource())
v1_api.register(AwardsResource())
v1_api.register(BadgesResource())
v1_api.register(RegisterResource())
v1_api.register(UserResource())

urlpatterns = patterns('',

    url(r'^$', 'oppia.views.home_view', name="oppia_home"),
    url(r'^upload/$', 'oppia.views.upload', name="oppia_upload"),
    url(r'^upload/success/$', TemplateView.as_view(template_name="oppia/upload-success.html"), name="oppia_upload_success"),
    url(r'^course/$', 'oppia.views.course_view', name="oppia_course"),
    url(r'^course/(?P<id>\d+)/$', 'oppia.views.recent_activity', name="oppia_recent_activity"),
    url(r'^course/(?P<id>\d+)/detail/$', 'oppia.views.recent_activity_detail', name="oppia_recent_activity_detail"),
    url(r'^course/(?P<course_id>\d+)/schedule/$', 'oppia.views.schedule', name="oppia_schedules"),
    url(r'^course/(?P<course_id>\d+)/schedule/add/$', 'oppia.views.schedule_add', name="oppia_schedule_add"),
    url(r'^course/(?P<course_id>\d+)/schedule/(?P<schedule_id>\d+)/edit/$', 'oppia.views.schedule_edit', name="oppia_schedule_edit"),
    url(r'^course/(?P<course_id>\d+)/schedule/saved/$', 'oppia.views.schedule_saved'),
    url(r'^course/(?P<course_id>\d+)/schedule/(?P<schedule_id>\d+)/saved/$', 'oppia.views.schedule_saved'),
    url(r'^course/(?P<course_id>\d+)/cohort/$', 'oppia.views.cohort', name="oppia_cohorts"),
    url(r'^course/(?P<course_id>\d+)/cohort/add/$', 'oppia.views.cohort_add', name="oppia_cohort_add"),
    url(r'^course/(?P<course_id>\d+)/cohort/(?P<cohort_id>\d+)/edit/$', 'oppia.views.cohort_edit', name="oppia_cohort_edit"),
    #url(r'^course/(?P<course_id>\d+)/cohort/(?P<cohort_id>\d+)/delete/$', 'oppia.views.cohort_delete', name="oppia_cohort_delete"),
    url(r'^profile/', include('oppia.profile.urls')),
    url(r'^terms/$', 'oppia.views.terms_view', name="oppia_terms"),
    
    url(r'^api/', include(v1_api.urls)),
    url(r'^quiz/', include('oppia.quiz.urls')),
    
    

)