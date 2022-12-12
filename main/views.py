from django.shortcuts import render
from .models import User
from .forms import UserForm
# Create your views here.
def subscribe(request):
    user = User.objects.all()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    else: form = UserForm()
    
    return render(request,
                  'main/subscribe_page.html',
                  {'user':user,
                   'form':form})