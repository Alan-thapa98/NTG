"""getanswer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# for the image
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve

from django.urls import path, include
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "GetAnswer Admin"
admin.site.site_title = "GetAnswer Admin Panel"
admin.site.index_title = "Welcome to GetAnswer Admin Panel"

urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('QandA/', include('question_answer.urls')),
    path('all_games/', include('games.urls')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('essay_and_bio/', include('essay_and_bio.urls', namespace='essay_and_bio')),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('blog', include('blog.urls')),
]
handler404 = "home.views.error_404"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
