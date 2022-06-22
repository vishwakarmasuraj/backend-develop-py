from django import views
from django.contrib import admin
from django.urls import path,include    
from . import views

urlpatterns = [
    #  path('admin/', admin.site.urls),
    path("list", views.stdList),
    path("login/", views.login),
    path("update/<int:id>", views.stdUpdate),
    path("del/<int:id>", views.stdDel),

]