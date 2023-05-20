from django.urls import path
from task_manager.labels import views

urlpatterns = [
    path('', views.LabelsPage.as_view(), name='labels_page'),
    path('create/', views.CreateLabelPage.as_view(), name='create_label'),
    path('<int:pk>/update/', views.UpdateLabelPage.as_view(), name='update_label'),
    path('<int:pk>/delete/', views.DeleteLabelPage.as_view(), name='delete_label'),
]
