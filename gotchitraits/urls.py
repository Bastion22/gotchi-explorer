
from django.contrib import admin
from django.urls import path

from app.views import home_view, gotchi_view, about_view, contact_view, nrg_view, agg_view, spk_view, brn_view, eys_view, eyc_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home_view'),
    path('gotchi/<int:gotchi_id>/', gotchi_view, name='gotchi_url'),
    path('about/', about_view, name='about_view'),
    path('contact/', contact_view, name='contact_view'),
    path('nrg/', nrg_view),
    path('agg/', agg_view),
    path('spk/', spk_view),
    path('brn/', brn_view),
    path('eys/', eys_view),
    path('eyc/', eyc_view),
]
