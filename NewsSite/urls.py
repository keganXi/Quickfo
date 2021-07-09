"""NewsSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path, include
from technology import views as tech_views
from entertainment import views as entertainment_views
from sports import views as sports_views
from django.conf.urls import handler404, handler500


urlpatterns = [
    path('', include('home.urls')),
    url(r'^Technology/$', tech_views.technology, name='tech-page'),
    url(r'^Technology/technologyloadstories/$', tech_views.load_more, name='tech_loader'),
    url(r'^Entertainment/$', entertainment_views.entertainment, name='entertainment-page'),
    url(r'^Entertainment/entertainmentloadstories/$', entertainment_views.load_more, name="entertainment_loader"),
    url(r'^Sports/$', sports_views.sports, name='sports-page'),
    url(r'^Sports/sportsloadstories/$', sports_views.load_more, name="sports_loader"),
    path('admin/', admin.site.urls),
]


handler404 = tech_views.error_404
handler500 = tech_views.error_500
