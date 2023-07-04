from django.contrib import admin
from django.urls import path, include
from . import views 

app_name = 'home'
urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name='about'),
    path('dictionary', views.dictionary, name='dictionary'),
    path('login',views.handeLogin, name='handeLogin' ),
     
    # path('search', views.search, name='search'),
    path('search_qanda', views.search_qanda, name='search_qanda'),
    path('search_essays', views.search_essays, name='search_essays'),
    path('all_class/<str:class_name>', views.all_class, name='all_class'),
    
    path('aboutus', views.aboutus, name="aboutus"),
    path('contactus', views.contactus, name="contactus"),
    path('policy_privacy', views.policy_privacy, name="policy_privacy"),
    path('termsandcontions', views.termsandcontions, name="termsandcontions"),

     
]
