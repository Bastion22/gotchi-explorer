from django import forms

#create your forms here

class GotchiForm(forms.Form):
    gotchi_id = forms.IntegerField(max_value=25000 ,required=True, widget=forms.TextInput(attrs={'class': "form-control"}), label='')
    
class WearableForm(forms.Form):
    wearable_id = forms.IntegerField(max_value=315 ,required=True, widget=forms.TextInput(attrs={'class': "form-control"}), label='')