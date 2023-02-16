
from django.contrib import admin
from django.urls import path

from app.views import home_view, gotchi_view, about_view, contact_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home_view'),
    path('gotchi/<int:gotchi_id>/', gotchi_view, name='gotchi_url'),
    path('about/', about_view, name='about_view'),
    path('contact/', contact_view, name='contact_view'),
]
