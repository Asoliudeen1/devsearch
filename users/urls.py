from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    
    path('', views.profiles, name="profiles"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('account/', views.userAccount, name="account"),
    path('edit-account/', views.editAccount, name="edit-account"),
    path('create-skill/', views.createSkill, name="create-skill"),
    path('update-skill/<str:pk>/', views.updateSkill, name="update-skill"),
    path('delete-skill/<str:pk>/', views.deleteSkill, name="delete-skill"),
    path('inbox/', views.Inbox, name="inbox"),
    path('messagedetail/<str:pk>/', views.MessageDetails, name="messagedetails"),
    path('createmessage/<str:pk>/', views.CreateMessage, name="createmessage"),
]