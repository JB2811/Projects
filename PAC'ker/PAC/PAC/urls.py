"""
URL configuration for PAC project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from seller import views
from buyer import views as v2
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('shopinterface/seller/takein/',views.takin),
    path('shopinterface/addshop/shopreg/',views.shopreg),
    path('shopinterface/seller/takein/',views.sell),
    path('shopinterface/del/deletein',views.delin),
    path('shopinterface/update/updatein',views.updatein),
    path('shopinterface/',views.shopin),
    path('shopinterface/addshop/',views.adds),
    path('shopinterface/seller/',views.sell,name='seller'),
    path('shopinterface/del/',views.de,name='del'),
    path('shopinterface/update/',views.up,name='update'),
    path('shopinterface/update/updateind',views.updaterec),
    path('buyer/',v2.buy),]
