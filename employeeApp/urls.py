# from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    # url('admin/', admin.site.urls),
    # path('student/', include('student.urls')),
    path('employee/', include('employeeCrud.urls')),
]