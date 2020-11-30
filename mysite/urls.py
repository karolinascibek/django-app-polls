"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from account import views as account_views
from account.auth import views as auth_views
from polls.questionnaire import views as polls_questionary_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', account_views.index, name='index'),

    path('register/', auth_views.register_view, name='register'),
    path('login/', auth_views.login_view, name='login'),
    path('logout/', auth_views.logout_view, name='logout'),

    #path('user/', account_views.profile_view, name='profile'),
    path('u/', account_views.update_profile_view, name='update_profile'),
    path('u/password-change', account_views.password_change_view, name='password_change'),
    path('u/delete', account_views.delete_profile_view, name='delete_profile'),

    path('u/questionnaire', polls_questionary_view.questionnaire_create_view, name='create_questionnaire'),
    path('u/questionnaire/<int:id>', polls_questionary_view.questionnaire_detail_view, name='detail_questionnaire'),
]


