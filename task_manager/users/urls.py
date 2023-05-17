from django.urls import path
from task_manager.users import views

urlpatterns = [
    path('', views.UsersPage.as_view(), name='users_page'),
    path('create/', views.CreateUserPage.as_view(), name='create_user'),
    path('<int:pk>/update/', views.UpdateUserPage.as_view(), name='update_user'),
    path('<int:pk>/delete/', views.DeleteUserPage.as_view(), name='delete_user'),
]
