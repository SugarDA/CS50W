from django.urls import path
from . import views
urlpatterns = [
    path("",views.index, name="index"),
    path("adnan",views.adnan, name="adnan"),
    path("<name>",views.greet, name="greet"),
    ]