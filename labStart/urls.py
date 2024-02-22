from django.urls import path
from . import views

urlpatterns =[
    path("", views.index, name="test"),
    path("<int:price>",views.taxCal),
    path("taxrate",views.taxrate)
]