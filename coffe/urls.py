from django.urls import path
from . import views

urlpatterns=[
    path('index/',views.index,name='index'),
    path('menu/',views.menu,name='menu'),
    path('contacto/',views.contacto,name='contacto'),
    path('about/',views.about,name='about'),
    path('salir/',views.salir,name='salir'),
    path('login/',views.login,name='login'),
    path('productos/',views.producto,name='productos'),
    path('nueva_cat/',views.N_categoria,name='new'),
    path('nueva_cat/0',views.N_categoria,name='new'),
    path('nueva_cat/<str:id>',views.N_cat_prod,name='new_id'),
    path('add/',views.add_prod,name='add'),
    path('BD/',views.list_prod,name='BD'),
    path('BD/',views.cruD,name='BD/ADD'),
    path('BD/<str:id>',views.del_prod,name='dele'),
    path('BD/<str:id>',views.edi_prod,name='editar'),
    path('contacto',views.contac,name='contacto'),


    path('pedido/',views.pedidos,name='pedidos'),
    path('pedido/0',views.pedidos,name='pedidos'),
     path('pedido/<str:id>',views.pedidosP,name='pedidos'),

]