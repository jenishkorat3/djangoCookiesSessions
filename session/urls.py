from django.urls import path
from . import views

urlpatterns = [
    path('set/', views.set_session, name='set_session'),
    path('get/', views.get_session, name='get_session'),
    path('del/', views.delete_session, name='delete_session'),
    path('flush/', views.flush_session, name='flush_session'),
    path('sessionmethodsinview/', views.sessionmethodsinview,
         name='sessionmethodsinview'),
    path('sessionclear/', views.sessionclear, name='sessionclear'),
    path('sessionmethodsintemplate/', views.sessionmethodsintemplate,
         name='sessionmethodsintemplate'),
    path('settestcookie/', views.settestcookie, name='settestcookie'),
    path('checktestcookie/', views.checktestcookie, name='checktestcookie'),
    path('deletetestcookie/', views.deletetestcookie, name='deletetestcookie'),
]
