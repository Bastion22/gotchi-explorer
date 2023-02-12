
from django.contrib import admin
from django.urls import path

from app.views import home_view, gotchi_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home_view'),
    path('gotchi/<int:gotchi_id>/', gotchi_view, name='gotchi_url'),
]
