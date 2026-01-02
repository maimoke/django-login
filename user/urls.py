from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sign-in/",views.sign_in, name="sign-in"),
    path("sign-up/",views.sign_up, name="sign-up"),
    path("sign-out/",views.sign_out, name='sign-out'),
    path("getuser",views.get_users_as_json, name='getuser'),
    path("adduser",views.add_user,name='adduser'),
    path("passwordchange",views.password_change,name='passwordchange'),
    path("deleteuser",views.delete_user,name='deleteuser')
]