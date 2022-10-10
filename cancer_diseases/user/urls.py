from django.urls import path
from .import views


urlpatterns=[

    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('register',views.register,name='reg'),
    path('lcancer',views.lungcancer,name='lcancer'),
    path('prediction',views.prediction,name='prediction'),
    path('lungpredict',views.Predictlung,name='lungpredict'),
   

]