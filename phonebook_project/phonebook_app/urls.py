from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.addphonenumber),
    path('display/', views.displaylist, name='displaylist'),
    path('delete/', views.deletephone, name='deletephone'),
    path('update/', views.updatename, name='updatename'),
]