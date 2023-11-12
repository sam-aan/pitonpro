from django.shortcuts import render, redirect
from .forms import solvedom
from .models import SolVed

def sol_ved(request, data=None):
    error = ''

    if request.method == 'POST':
        form = solvedom(request.POST, request.FILES)

        if form.is_valid():
            form = form.save(commit=False)
            uploadedFile = request.FILES["uploadedFile"]
            print(uploadedFile, form.NomProj_id)
            form.Responsible = request.user.first_name + ' ' + request.user.last_name
            form.save()
            print(form.NomZak, form.NomProj_id, uploadedFile, form.PromPlosh)
            return redirect('zakazi')
        else:
            error = 'какая то ху...я'

    form = solvedom
    content = {
        'form': form,
        'error': error,
        'title': 'Солярис Ведомость'
    }
    return render(request, 'solaris_vedomost/solaris_vedomost.html', content)

def spis_zakaz(request):
    date_spis_zakaz = SolVed.objects.all()
    return render(request, 'solaris_vedomost/spis_zakaz.html',
                  {'title': 'Зарегистрированные Заказы', 'date_spis_zakaz': date_spis_zakaz})
