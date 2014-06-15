from django.conf.urls import patterns, include, url
from django.contrib import admin

from tastypie.api import Api

from studentAPI.api import CandidateResource, DepartmentResource


v1_api = Api(api_name='v1')
v1_api.register(CandidateResource())
v1_api.register(DepartmentResource())

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^api/', include(v1_api.urls)),
                       )
