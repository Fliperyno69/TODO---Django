from django.urls import path
from django.contrib.auth import views as auth_views
from curaku import views

urlpatterns = [
    # User authentication URLs
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),  # Redirect to 'home' after logout

    # Task management URLs
    path('task/create/', views.task_create, name='task_create'),
    path('task/<int:id>/complete/', views.task_complete, name='task_complete'),
    path('', views.home, name='home'),  # Home page that also displays tasks
    path('tasks/', views.task_list, name='tasks'),  # Ensure the URL pattern has the name 'tasks'
    path('task/create/', views.task_create, name='task_create'),  # URL to create a new task
    path('task/<int:id>/update/', views.task_update, name='task_update'),  # URL to update a task
    path('task/<int:id>/delete/', views.task_delete, name='task_delete'),  # URL to delete a task
]

