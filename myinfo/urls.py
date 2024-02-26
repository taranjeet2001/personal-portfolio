from django.urls import path
from .views import *


urlpatterns = [
    path('',view_home , name='home'),
    path("save/",view_save_data,name='savedata'),

]
