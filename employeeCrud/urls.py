from django.urls import path
from .views import EmployeeCreateApi,EmployeeApi,EmployeeUpdateApi,EmployeeDeleteApi

urlpatterns = [
    path('api',EmployeeApi.as_view(), name='employee-list'),
    path('api/create',EmployeeCreateApi.as_view(), name='employee-create'),
    path('api/<int:pk>',EmployeeUpdateApi.as_view(), name='employee-detail-update'),
    path('api/<int:pk>/delete',EmployeeDeleteApi.as_view(), name='employee-delete'),
]
