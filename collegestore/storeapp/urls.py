from django.urls import path,include
from .import views
app_name='storeapp'


urlpatterns=[

     path('',views.index,name='index'),

]


