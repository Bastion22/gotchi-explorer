
from django.contrib import admin
from django.urls import path

from app.views import home_view, about_view, contact_view, nrg_view, agg_view, spk_view, brn_view, eys_view, eyc_view

from app.views import explore_gotchi_view, explore_wearable_view

from app.views import gotchi_view, wearable_view

from app.views import tools_view

from app.views import portal_counter_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home_view'),
    
    path('gotchi/', explore_gotchi_view, name='explore_gotchi'),
    path('wearable/', explore_wearable_view, name='explore_wearable'),
    
    path('gotchi/<int:gotchi_id>/', gotchi_view, name='gotchi_url'),
    path('wearable/<int:wearable_id>/', wearable_view, name='wearable_url'),
    
    path('tools/', tools_view, name='tools_view'),
    
    path('tools/portalCounter/', portal_counter_view, name='portal_counter_view'),
    
    path('about/', about_view, name='about_view'),
    path('contact/', contact_view, name='contact_view'),
    path('nrg/', nrg_view),
    path('agg/', agg_view),
    path('spk/', spk_view),
    path('brn/', brn_view),
    path('eys/', eys_view),
    path('eyc/', eyc_view),
]
