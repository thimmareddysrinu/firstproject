from django.urls import path
from ecommerceapp import views


urlpatterns = [
    path("",views.index,name='index'),
    path("contact",views.contact,name='contact'),
    path("about",views.about,name='about'),
    path("profile", views.profile, name='profile'),
    path("home",views.home,name='home'),
    path("checkout/",views.checkout,name="checkout"),
    path('shopcart',views.shopcart,name='shopcart'),
    path('handlerequest', views.handlerequest, name="HandleRequest"),

    
    
]
