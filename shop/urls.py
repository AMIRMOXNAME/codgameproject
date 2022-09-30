from django.urls import path
from . import views
from .views import *
app_name="post"
urlpatterns = [
    path('' , views.index , name='index'),
    path('tozihat/<slug:slug>' , detail , name="detail"),
    path('dashboard/' , views.dashboard , name="dashboard"),
    path('login/' , views.user_login , name="login"),
    path('logout/' , views.user_logout , name="logout"),
    path('signup/' , views.user_signup , name="signup"),
]
