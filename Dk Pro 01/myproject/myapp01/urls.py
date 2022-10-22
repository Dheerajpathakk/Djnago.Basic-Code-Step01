from django.urls import path
from myapp01 import views
urlpatterns=[
    path("",views.registration,name="home")
]