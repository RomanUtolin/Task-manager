from django.urls import path
from task_manager.tasks import views

urlpatterns = [
    path('', views.TasksPage.as_view(), name='tasks_page'),
    path('create/', views.CreateTaskPage.as_view(), name='create_task'),
    path('<int:pk>/', views.OpenTaskPage.as_view(), name='open_task'),
    path('<int:pk>/update/', views.UpdateTaskPage.as_view(), name='update_task'),
    path('<int:pk>/delete/', views.DeleteTaskPage.as_view(), name='delete_task'),
]
