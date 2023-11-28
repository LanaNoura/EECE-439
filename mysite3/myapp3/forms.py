from django import forms
from .models import ContactList 

class ContactListForm(forms.ModelForm):
    class Meta:
        model = ContactList
        fields = ['name', 'email', 'date_joined', 'date_expired']

        widgets = {
            'date_joined': forms.TextInput(attrs={'type': 'date'}),
            'date_expired': forms.TextInput(attrs={'type': 'date'}),
        }

    def clean_date_expired(self):
        date_joined = self.cleaned_data.get('date_joined')
        date_expired = self.cleaned_data.get('date_expired')

        if date_joined and date_expired and date_expired < date_joined:
            raise forms.ValidationError("Date Expired cannot be before Date Joined.")

        return date_expired






