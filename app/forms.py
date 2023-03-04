from django import forms

#create your forms here

class GotchiForm(forms.Form):
    gotchi_id = forms.IntegerField(max_value=25000 ,required=True, widget=forms.TextInput(attrs={'class': "form-control"}), label='')
    # post = forms.IntegerField(max_value=25000 ,required=True, name="user_input")
    
class WearableForm(forms.Form):
    wearable_id = forms.IntegerField(max_value=369 ,required=True, widget=forms.TextInput(attrs={'class': "form-control"}), label='')