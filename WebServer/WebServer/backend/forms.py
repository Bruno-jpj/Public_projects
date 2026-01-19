from django import forms
from .models import Site
#
# creazione di un form che si collega al modello per l'inserimento dei campi nel db
class SiteCreateForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = [
            'title',
            'description',
            'category',
            'paid',
            'url'
        ]
        # Serve solo a modificare l’aspetto o il comportamento dei campi HTML generati da Django
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Titolo', 'maxlength': 128}),
            'description': forms.Textarea(attrs={'placeholder': 'Descrizione', 'rows': 4}),
            'paid':forms.CheckboxInput(),
            'url': forms.URLInput(attrs={'maxlength':256}),
        }