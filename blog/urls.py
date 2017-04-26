from django.conf.urls import url, include
import blog
from blog import views
from django.conf import settings


urlpatterns = {
    url(r'^$', blog.views.home, name='home'),
    url(r'about$', blog.views.about, name='about'),
    url(r"^article/(?P<article_id>[0-9]+)/$", blog.views.show_article, name='article'),
}