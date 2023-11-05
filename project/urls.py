
from django.contrib import admin
from django.urls import path
from app.views import ListNumber, CreateNumber


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', ListNumber.as_view(), name='list'),
    path('create/', CreateNumber.as_view(), name='create')
]
