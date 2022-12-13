from django import forms
from .models import User, Contact

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'description']