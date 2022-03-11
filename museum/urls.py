from django.urls import path
from . import views

urlpatterns = [
    path('galery', views.galery, name='galery'),
    path('', views.main, name="main"),
    path('photoB', views.photoB, name="photoB"),
    path('portal', views.portal, name="portal"),
    path('portal2', views.portal2, name="portal2"),
    path('statistica_polz', views.statistica_polz, name="statistica_polz"),
    path('navi/gid/exp1', views.exp1, name="exp1"),
    path('navi/gid/exp2', views.exp2, name="exp2"),
    path('navi/gid/exp3', views.exp3, name="exp3"),
    path('navi/gid/exp4', views.exp4, name="exp4"),
    path('navi/gid/exp5', views.exp5, name="exp5"),
    path('navi/gid/exp6', views.exp6, name="exp6"),
    path('navi/gid/exp7', views.exp7, name="exp7"),
    path('navi/gid/exp8', views.exp8, name="exp8"),
    path('navi', views.navi, name="navi"),
    path('navi/gid', views.gid, name="gid"),
    path('statCrit1', views.statCrit1, name="statCrit1"),
    path('posesch', views.posesch, name="posesch"),
    path('statistica_polz', views.statistica_polz, name="statistica_polz"),
    path('login', views.login, name="login"),
    path('admstat', views.admstat, name="admstat"),
    path('exponats', views.exponats, name="exponats"),
]