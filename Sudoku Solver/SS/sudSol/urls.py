from django.urls import path
from .import views
urlpatterns=[path('',views.test),
 	         path('solvefrnd/',views.t1),
             path('cdisp/',views.test1),
             path('game/',views.game),
             path('easy/',views.easy),
             path('medium/',views.medium),
             path('hard/',views.hard),]