from django.shortcuts import render, redirect

from .forms import GotchiForm
from .scrapers.gotchi_scraper import GotchiScraper

# Create your views here.

def home_view(request):
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
    
    return render(request, 'home.html', context)


def gotchi_view(request, gotchi_id):
    
    try:
        gotchi_obj = GotchiScraper(gotchi_id) # Initialize
        return_stats = gotchi_obj.get_stats() # Call
        return_svg = gotchi_obj.get_svg() # Call
        
    except:
        return render(request, 'error.html', {'id': id})
        
    context = {
        # 'svg_list': svg_data_list,
        'text_stat_list': return_stats,
        'return_svg': return_svg,
    }
    return render(request, 'gotchi.html', context=context)  
