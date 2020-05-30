from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

from .forms import dataBaseForm
from django_simfuel.views import navBarUserName
@staff_member_required()
def registerPage(request):
    form = dataBaseForm()
    userInfo = navBarUserName(request)
    if request.method == 'POST':
        form = dataBaseForm(request.POST)
        if form.is_valid():
            form.save()
            form = dataBaseForm()
    context = {'form':form,
              }
    context = {**context, **userInfo}
    return render(request, 'databases/registerDB.html', context)