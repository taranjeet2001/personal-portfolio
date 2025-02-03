from django.urls import path
from .views import *


urlpatterns = [
    path('',view_home , name='home'),
    path('send-email/', send_contact_email, name='send_contact_email'),

]
