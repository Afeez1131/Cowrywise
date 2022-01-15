from django.urls import include, path

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
# from api.views import ApiViewSet
from . import views


urlpatterns = [
   path('', views.api_list),

]

urlpatterns = format_suffix_patterns(urlpatterns)
