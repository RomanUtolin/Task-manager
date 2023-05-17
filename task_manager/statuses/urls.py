from django.urls import path
from task_manager.statuses import views

urlpatterns = [
    path('', views.StatusesPage.as_view(), name='statuses_page'),
    path('create/', views.CreateStatusPage.as_view(), name='create_status'),
    path('<int:pk>/update/', views.UpdateStatusPage.as_view(), name='update_status'),
    path('<int:pk>/delete/', views.DeleteStatusPage.as_view(), name='delete_status'),
]
