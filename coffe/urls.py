from django.urls import path
from . import views

urlpatterns=[
    path('index/',views.index,name='index'),
    path('productos/',views.producto,name='productos'),
    path('add/',views.add_prod,name='add'),
    path('BD/',views.list_prod,name='BD'),
    path('BD/<str:id>',views.del_prod,name='dele'),

]