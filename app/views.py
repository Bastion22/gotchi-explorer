import json

from django.shortcuts import render, redirect

from .forms import GotchiForm
from .forms import WearableForm
from .scrapers.gotchi.gotchi_scraper import GotchiScraper
from .scrapers.wearable.wearable_scraper import WearableScraper


import os

# Get the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Create the path to the subdirectory relative to the current directory
folder_path = os.path.join(current_dir, 'data_libraries', 'portal_supply')


# Create your views here.

def home_view(request):
    return render(request, 'home.html')


def explore_gotchi_view(request):
    form = GotchiForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            gotchi_id = form.cleaned_data['gotchi_id']
            return redirect('gotchi_url', gotchi_id=gotchi_id)
        
    context = {
        'form': form,
    }
    
    return render(request, 'explore/explore_gotchi.html', context)


def explore_wearable_view(request):
    form = WearableForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            wearable_id = form.cleaned_data['wearable_id']
            return redirect('wearable_url', wearable_id=wearable_id)
       
    context = {
        'form': form,
        }
    
    return render(request, 'explore/explore_wearable.html', context)


def gotchi_view(request, gotchi_id):
    
    try:
        gotchi_obj = GotchiScraper(gotchi_id) # Initialize
        return_stats = gotchi_obj.get_stats() # Call
        return_svg = gotchi_obj.get_svg() # Call
        
    except:
        return render(request, 'errors/gotchi_not_found.html', {'id': gotchi_id})
        
    context = {
        # 'svg_list': svg_data_list,
        'gotchi_id': gotchi_id,
        'return_stats': return_stats,
        'return_svg': return_svg,
    }
    return render(request, 'gotchi.html', context=context)  


def wearable_view(request, wearable_id):
    
    try:
        wearable_obj = WearableScraper(wearable_id) # Initialize
        return_svg = wearable_obj.get_svg() # Call get_svg
        return_name = wearable_obj.get_name() # Call get_name
        return_trait_modifiers = wearable_obj.get_trait_modifiers()
        
    except:
        return render(request, 'errors/wearable_not_found.html', {'id': wearable_id})
        
    context = {
        # 'svg_list': svg_data_list,
        'return_svg': return_svg,
        'return_name': return_name,
        'return_trait_modifiers': return_trait_modifiers,
    }
    
    return render(request, 'wearable.html', context=context)  

def tools_view(request):
    
    return render(request, 'tools/tools.html')


def portal_counter_view(request):
    
    
    with open(os.path.join(folder_path, 'h1_supply.json'), 'r') as f:
        h1_portals = json.load(f)
        
    with open(os.path.join(folder_path, 'h2_supply.json'), 'r') as f:
        h2_portals = json.load(f)
    
    context = {
        'h1_portals': h1_portals,
        'h2_portals': h2_portals,
    } 
    
    return render(request, 'tools/tool_list/portals.html', context=context)




def about_view(request):
    
    return render(request, 'about.html')


def contact_view(request):
    
    return render(request, 'contact.html')


def nrg_view(request):
    return render(request, 'stats/attributes/nrg.html')

def agg_view(request):
    return render(request, 'stats/attributes/agg.html')

def spk_view(request):
    return render(request, 'stats/attributes/spk.html')

def brn_view(request):
    return render(request, 'stats/attributes/brn.html')

def eys_view(request):
    return render(request, 'stats/attributes/eys.html')

def eyc_view(request):
    return render(request, 'stats/attributes/eyc.html')
