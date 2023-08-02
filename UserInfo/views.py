from django.shortcuts import render, redirect
from .forms import UserInfoForm

def UserInfo(request):
    error = ''
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/success')
        else:
            print(form.errors)
            error = 'Форма была отправлена неверной'
    form = UserInfoForm()


    data = {
        'form' : form,
        'error' : error
    }

    return render(request, 'UserInfo.html', data)

def success(request):
    return render(request, 'succes.html')
