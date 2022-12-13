from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import User
from .forms import UserForm, ContactForm

# Create your views here.

def subscribe(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else: form = UserForm()
    
    return render(request,
                  'main/subscribe.html',
                  {'form':form})

# def unsubscribe(request):
#     user = User.objects.get('email')
#     if user == request.get():
#         if user['active'] == False :
#             return redirect('success')
        
    
#     return render(request, 
#                   'main/subscribe.html',
#                   {'user':user})

def home(request):
    
    return render(request,
                  'main/home.html')
    
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else: form = ContactForm()    
    
    return render(request,
                  'main/contact.html',
                  {'form':form})
    
def success(request):
    return render(request, 'main/success.html')