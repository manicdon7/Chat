from django.urls import path
from . import views

urlpatterns = [
    path('/',views.index,name='Index'),
    path('friend/<str"pk>',views.detail,name="detail")
]
