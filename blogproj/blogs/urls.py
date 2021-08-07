from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from .views import home_view,detailed_view,category_view,list_all_view
app_name = 'blogs'
urlpatterns = [

    path('', home_view,name='home'),
    path('categories/<str:category>/<str:title>/',detailed_view,name="details"),
    path('categories/',category_view,name="categories"),
    path('categories/<str:category>/',list_all_view)

]
