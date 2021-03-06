"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from django.contrib import admin
from api.api_view import api_movie_list_create, api_movie_detail
from rest_framework.authtoken import views

from movie.views import MovieListView, MovieCreateView, MovieDeleteView, MovieDetailView


urlpatterns = [
    url(r'^movie_list/', MovieListView.as_view(), name="movie_list"),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^api/', include('api_framework.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^movie/$', api_movie_list_create, name="create_movie"),
    url(r'^movie/detail/(?P<pk>\d+)/$',api_movie_detail, name="delete_movie")
]
