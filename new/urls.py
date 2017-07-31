"""new URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import views as auth_views
from django.contrib.contenttypes import views as contenttypes_views
from django.contrib.flatpages.sitemaps import FlatPageSitemap
from django.contrib.sitemaps import views as sitemap_views
from django.views.decorators.cache import cache_page
from django.views.generic import RedirectView, TemplateView
from django.views.static import serve
from markdownx.views import MarkdownifyView



urlpatterns=[
    url('^admin/',include(admin.site.urls)),
    url('^accounts/',include('registration.backends.hmac.urls')),
    url('^$',TemplateView.as_view(template_name='registration/base/index.html'),name='index'),
    url('^accounts/profile/',TemplateView.as_view(template_name='registration/base/profile.html'),name='profile'),
]
