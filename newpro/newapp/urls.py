from newapp import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name='newapp'

urlpatterns=[
       path('',views.register,name='register'),
       path('login/',views.login_user,name='login_user'),
       

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
