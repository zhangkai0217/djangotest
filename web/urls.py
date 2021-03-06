"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import view
from web.userinfo.user_manage import user_manage
from web.userinfo import user_manage_new
from web.h5 import h5

urlpatterns = [
    path('admin/', admin.site.urls),
    path('runoob/', view.runoob),
    path('getUserList/', user_manage.get_user),
    path('UserListNew/', user_manage_new.post),
    path('createUser/', user_manage_new.add_user),
    path('addPwd/', user_manage_new.add_pwd),
    path('addUsTest/', user_manage_new.add_ustest),
    path('jianai/', h5.get_h5),
]
