from django.urls import path
from . import views
#from .views import TaskList

urlpatterns = [
    path('', views.index, name = "list"),
    path('update_task/<str:pk>/', views.updateTask, name = "update_task"),
    path('delete/<str:pk>/', views.deleteTask, name = "delete"),

    path('register/', views.registerPage, name = 'register'),
    path('login/', views.loginPage, name = 'login'),
    path('logout', views.logoutUser, name = 'logout'),

]
