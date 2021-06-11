from django.urls import path
from . import views

urlpatterns = [
    path("", views.add_show, name="addandshow"),
    path("signup", views.signuppage, name="signup"),
    path("login", views.loginpage, name="login"),
    path("logout", views.logoutpage, name="logout"),
    # path("adddata", views.addData, name="adddata"),
    path("delete/<int:id>/", views.delete_data, name="deletedata"),
    path("<int:id>/", views.update_data, name="updatedata"),
]
