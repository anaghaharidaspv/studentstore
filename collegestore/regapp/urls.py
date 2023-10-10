from .import views
from django.urls import path

urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('detailform', views.detailform, name='detailform'),
    path('bioscience',views.bioscience,name='bioscience'),
    path('compscience',views.compscience,name='compscience'),
    path('commerce',views.commerce,name='commerce'),
    path('humanties',views.humanties,name='humanties'),
    path('vhsc',views.vhsc,name='vhsc'),
]