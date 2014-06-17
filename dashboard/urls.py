from django.conf.urls import url
from django.conf.global_settings import STATICFILES_DIRS

from dashboard import views

urlpatterns = [
    # ex: /
    url(r'^$', views.index, name='index'),
]
