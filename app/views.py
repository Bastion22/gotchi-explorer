from django.shortcuts import render, redirect

from .forms import GotchiForm
from .forms import WearableForm
from .scrapers.gotchi_scraper import GotchiScraper

# Create your views here.

def home_view(request):
    return render(request, 'home.html')

def explore_gotchi_view(request):
    form = GotchiForm(request.POST or None)
    
    context = {
        
    }
    
    if form.is_valid():
        id_input = form.cleaned_data['gotchi_id']
        context['id_input'] = id_input
        form = GotchiForm()
        
    context['form'] = form
    
    if request.method == 'POST':
        gotchi_id = request.POST.get('gotchi_id')
        context['gotchi_id'] = gotchi_id
        return redirect('gotchi_url', gotchi_id=gotchi_id)
    
    return render(request, 'explore/explore_gotchi.html', context)


def explore_wearable_view(request):
    form = WearableForm(request.POST or None)
    
    context = {
        
    }
    
    if form.is_valid():
        id_input = form.cleaned_data['wearable_id']
        context['id_input'] = id_input
        form = WearableForm()
        
    context['form'] = form
    
    if request.method == 'POST':
        wearable_id = request.POST.get('wearable_id')
        context['wearable_id'] = wearable_id
        return redirect('wearable_url', wearable_id=wearable_id)
    
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
        'text_stat_list': return_stats,
        'return_svg': return_svg,
    }
    return render(request, 'gotchi.html', context=context)  

def wearable_view(request, wearable_id):
    
    try:
        wearable_obj = GotchiScraper(wearable_id) # Initialize
        return_modifications = wearable_obj.get_stats() # Call
        return_svg = wearable_obj.get_svg() # Call
        
    except:
        return render(request, 'errors/wearable_not_found.html', {'id': wearable_id})
        
    context = {
        # 'svg_list': svg_data_list,
        'text_stat_list': return_modifications,
        'return_svg': return_svg,
    }
    return render(request, 'wearable.html', context=context)  


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
