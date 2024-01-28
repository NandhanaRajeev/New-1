from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('contacts',views.contact,name="contact"),
    path('blog',views.blog,name="blog"),
    path('login',views.user_login,name="login"),
    path('register',views.register,name="register"),
<<<<<<< HEAD
    path('admin',views.admin,name="admin"),
=======
    path('tnc',views.tnc,name="tnc"),
>>>>>>> db7c3855c8103627b9dc557cc51315a666ce118f
    ]