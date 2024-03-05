from django.urls import path
from .import views

urlpatterns = [

    path('',views.index,name='index'),
    path('as_admin/login/', views.admin_login, name='admin_login'),
]