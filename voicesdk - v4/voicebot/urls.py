from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('submit_form/', views.submit_form, name='submit_form'),
    path('camera_feed/', views.camera_feed, name='camera_feed'),
    path('', views.form, name='form'),    
    path('exam/', views.exam, name='exam'),
    path('submit_answer/', views.submit_answer, name='submit_answer'),
    path('end_exam/', views.end_exam, name='end_exam'),
    path('guidelines/', views.guidelines, name='guidelines'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('home_page/',views.home_page,name='home_page'),
    path('mcq_exam_page/', views.mcq_exam_page, name='mcq_section'), 
    path('tf_exam_page/', views.tf_exam_page, name='tf_section'),  
    path('fib_exam_page/', views.fib_exam_page, name='fib_section'),  
    path('essay_exam_page/', views.essay_exam_page, name='essay_section'),  
    path('face_detection/', views.face_detection, name='face_detection'),
    path('log_event/', views.log_event, name='log_event'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
