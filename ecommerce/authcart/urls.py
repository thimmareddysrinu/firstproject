from django.urls import path
from authcart import views

urlpatterns = [
    path('signin',views.signin,name='signin'),
    path('login',views.handlogin,name='handlelogin'),
    path('logout',views.handlogout,name='handlelogout'),
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name='activate'),
   
]
