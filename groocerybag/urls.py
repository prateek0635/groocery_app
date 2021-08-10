
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    
    path('',views.home,name='home'),
    path('add',views.add_item,name='add_item'),
    path('sign-up',views.sign_up,name='sign_up'),
    path('log-in',views.log_in,name='log_in'),
    path('logout',views.log_out,name='log_out'),
    path('delete/<int:id>',views.delete_item,name='delete_item'),
    path('update/<int:id>',views.update_item,name='update')
]