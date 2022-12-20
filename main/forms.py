from django import forms
from .models import User, Contact

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']

    def validate_unique(self):
        pass

    def save(self):
        obj = super().save(commit=False)
        User.objects.update_or_create(email=obj.email, defaults={"active":True})
        
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'description']