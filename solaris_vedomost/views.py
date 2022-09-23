from django.shortcuts import render, redirect
from .forms import solvedom
import datetime

def sol_ved(request, data=None):
    error = ''

    if request.method == 'POST':
        form = solvedom(request.POST, request.FILES)

        if form.is_valid():
            form = form.save(commit=False)
            uploadedFile = request.FILES["uploadedFile"]
            print(uploadedFile)
            form.Responsible = request.user.first_name + ' ' + request.user.last_name
            form.save()
            return redirect('home')
        else:
            error = 'какая то ху...я'

    form = solvedom
    content = {
        'form': form,
        'error': error,
        'title': 'Солярис Ведомость'
    }
    return render(request, 'solaris_vedomost/solaris_vedomost.html', content)
