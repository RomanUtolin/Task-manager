from django.contrib import admin
from django.urls import path, include
from task_manager import views

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
    path('login/', views.LoginPage.as_view(), name='login_page'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('users/', include('task_manager.users.urls')),
    path('statuses/', include('task_manager.statuses.urls')),
    path('tasks/', include('task_manager.tasks.urls')),
    path('labels/', include('task_manager.labels.urls')),
]
