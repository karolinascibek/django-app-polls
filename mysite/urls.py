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
from polls.questionnaire import views as polls_questionnaire_view
from polls.questionnaire import api as polls_questionnaire_api
from polls.questionnaire.question import views as polls_question_view, api as polls_question_api
from polls.questionnaire.choice import api as polls_choice_api
from polls.respondents.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', account_views.index, name='index'),

    path('register/', auth_views.register_view, name='register'),
    path('login/',       auth_views.login_view, name='login'),
    path('logout/',     auth_views.logout_view, name='logout'),

    #path('user/', account_views.profile_view, name='profile'),
    path('u/',                 account_views.update_profile_view, name='update_profile'),
    path('u/password-change', account_views.password_change_view, name='password_change'),
    path('u/delete',           account_views.delete_profile_view, name='delete_profile'),

    path('questionnaire',          polls_questionnaire_view.questionnaire_create_view, name='create_questionnaire'),
    path('questionnaire/<int:id>', polls_questionnaire_view.questionnaire_detail_view, name='detail_questionnaire'),
    path('questionnaire/<int:id>/update', polls_questionnaire_view.questionnaire_update_view, name='update_questionnaire'),
    path('questionnaire/<int:id>/delete', polls_questionnaire_view.questionnaire_delete_view, name='delete_questionnaire'),
    path('questionnaire/<int:id>/share',   polls_questionnaire_view.questionnaire_share_view, name='share_questionnaire'),
    path('<str:questionnaire_code>',   polls_questionnaire_view.questionnaire_display_view, name='display_questionnaire'),

    path('questionnaire/<int:id>/new',        polls_question_view.question_create_view, name='create_question'),
    path('question/<int:id_question>/update', polls_question_view.question_update_view, name='update_question'),
    path('question/<int:id_question>/delete', polls_question_view.question_delete_view, name='delete_question'),
    # path('u/questionnaire/<int:id>/open-question/<int:id_question>', polls_question_view.open_question_update_view,
    #      name='update_open_question'),

    # respondents view
    path('respondent/questionnaires', respondent_questionnaires, name='respondent_questionnaires'),
    path('respondent/<id_questionnaire>', respondent_questionnaire, name='respondent_questionnaire'),

    # API
    path('api/questionnaire/<int:id>',  polls_questionnaire_api.detail_questionnaire, name='detail_questionnaire_api'),
    path('api/question/<int:id_question>',        polls_question_api.question_detail, name='detail_question_api'),
    path('api/question/<int:id_question>/update', polls_question_api.question_update, name='update_question_api'),
    # path('close-question/<int:id_question>/delete', polls_question_api.close_question_delete_api, name='close_question_delete_api'),
    path('api/choice/delete', polls_choice_api.choice_delete_api, name='delete_choice_api'),
    # # path('close-question/<int:id_question>/choice/create', polls_choice_api.choice_create_api, name='choice_create_api'),
    # # path('close-question/<int:id_question>/choice/update', polls_choice_api.choice_update_api, name='choice_update_api'),

]


