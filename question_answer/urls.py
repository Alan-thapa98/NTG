from django.contrib import admin
from django.urls import path, include
from question_answer import views
from .views import question_ansewr_UpdateView
app_name = "question_answer"

urlpatterns = [
    # answer questions page urls
    path('', views.all_questions_answers, name='all_questions_answers'),
    path('getanswer/<str:slug>',
         views.read_all_questions_answers, name='read_all_questions_answers'),

   # upload urls
    path('upload_qanda_on_getanswr_9813587726', views.upload_qanda_on_getanswr_9813587726,
         name='upload_qanda_on_getanswr_9813587726'),

    # Management urls
    path('dashboard_ans', views.dashboard_ans, name='dashboard_ans'),
    path('<str:slug>/update_ans', views.question_ansewr_UpdateView.as_view(), name='update_ans'),
    path('<str:slug>/delete_ans', views.delete_ans, name='delete_ans'),

]
