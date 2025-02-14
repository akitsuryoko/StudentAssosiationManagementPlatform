"""SAMP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path
from django.contrib.staticfiles.views import serve
from django.conf.urls.static import static
from . import view
from . import view_special
from . import userpage
from . import settings

urlpatterns = [
    path('', view.index),
    path('admin/', admin.site.urls),
    path('index/', view.index),
    path('login/', view.login),
    path('logout/', view.logout),
    path('register/', view.register),
    path('creatclub/', view.creatclub),
    path('searchclub/', view.searchclub),
    path('userpage/', userpage.userpage),
    path('favicon.ico', serve, {'path': '../static/pictures/pikachu2.jpg'}),

    #re_path(r'.', view.redir_to_index),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# handler500 = view.
handler404 = view_special.page_not_found