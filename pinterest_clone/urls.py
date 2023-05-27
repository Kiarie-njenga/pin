"""pinterest_clone URL Configuration
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from pins.sitemaps import PinSitemap
sitemaps = {
    "pins": PinSitemap,
    
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('debug/', include('debug_toolbar.urls')),
    path('', include('pinterest.urls', namespace='pinterest')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('boards/', include('boards.urls', namespace='boards')),
    path('pins/', include('pins.urls', namespace='pins')),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)