from django.urls import path
from . import views


urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),

    #path('pageindex', views.pageindex, name="pageindex"),

    path('searchpage', views.multiplesearch, name="searchpage"),

    path('page1', views.invdisplay, name="invdisplay"),
    path('Create', views.invinsert, name="invinsert"),
    path('Create1', views.invinsert1, name="invinsert1"),
    path('Edit1/<int:id>', views.invedit, name="invedit"),
    path('Update1/<int:id>', views.invupdate, name="invupdate"),
    path('Delete1/<int:id>', views.invdel, name="invdel"),

    path('page2', views.sitedisplay, name="sitedisplay"),
    path('Create2', views.siteinsert,name="siteinsert"),
    path('Edit2/<int:id>', views.siteedit, name="siteedit"),
    path('Update2/<int:id>', views.siteupdate, name="siteupdate"),
    path('Delete2/<int:id>', views.sitedel, name="sitedel"),

    path('page3', views.webpage3, name="webpage3"),

    path('products/', views.products, name='products'),
    path('customer/<str:pk_test>/', views.customer, name="customer"),
    path('customer1/<str:pk_test>/', views.customer1, name="customer1"),

    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),


]