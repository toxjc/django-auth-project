from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.update_profile, name='update_profile'),
    path('delete/', views.delete_account, name='delete_account'),

    # API для администратора
    path('admin/roles/', views.role_list_create, name='role-list-create'),
    path('admin/permissions/', views.permission_list_create, name='permission-list-create'),
    path('admin/assign-role/', views.assign_role_to_user, name='assign-role-to-user'),
    path('admin/assign-permission/', views.assign_permission_to_role, name='assign-permission-to-role'),
]