from django.urls import path
from todoapp import views

urlpatterns = [
    path('home',views.index),
    path('edit/<rid>',views.edit),
    path('delete/<rid>',views.delete),
    path('index',views.home),
    path('contact',views.contact),
    path('products',views.products),
    path('blog',views.blog),
    path('store',views.store),
    path('pdashboard',views.dash_product)

    
]
''' urlpatterns list contain list of patterns of urls
    we need a function to define paths
    path('url to be mapped',views.functionname,name=urlname)
    urlmapping from django server  is mapped to  url to be mapped in this fnc
    client --->/contact to django server
                     |
                     |
                     V
                     urls.py
    urlpatternslist[
    |
    |
    V
    path(' first parameter mapped here')
    if matched then or else NOT FOUND 404
    |
    |
    V
    views.py ---> respective functionaname() will be invoked
    this functioname() should provide response to the user

    RESPONSE _____|
    |
    |
    V


'''