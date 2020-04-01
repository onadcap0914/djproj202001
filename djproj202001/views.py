from django.shortcuts import render, redirect   #[4]
from django.contrib.auth.forms import UserCreationForm      #[4]
from django.contrib.auth.decorators import login_required   #[9]

"""
[2] onad | 20200324 | File first update
[3] onad | 20200326 | improvement of [2]
[4] onad | 20200330 | Application Home page and sign up functionality
[9] onad | 20200401 | Protected/secured views
"""
# Create your views here.


def home(request):
    title = 'CEU Credit Cooperative Management System'
    return render(request, 'home.html', {'title': title})   #[3] [4]


def signup(request):    #[4]
    title = 'CEU CC Management System User Registration'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('site_home')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'title': title,
                                                        'form': form})

#[9]
@login_required
def user_home(request):
    return render(request, 'user_home.html')
