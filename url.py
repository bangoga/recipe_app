from django.urls import include, path
from . import views
from django.conf.urls import url

"This is the main url setting for the current app, if you are navigating no where, you show views.index"
urlpatterns=[
    path('',views.index,name='index'),
    path('foodsrch/search_result_list',views.result,name="search_result_list"),
    path('foodsrch/search_result_list',views.index,name="search_result_list")
]