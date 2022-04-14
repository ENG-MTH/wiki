from django import forms

class EntryCreateForm(forms.Form):
    title= forms.CharField()
    content= forms.CharField(
        widget=forms.Textarea(attrs= {'cols': 40, 'rows': 5, 'style': 'height:100px'})
    )