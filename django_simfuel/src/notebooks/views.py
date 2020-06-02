from django.shortcuts import render, redirect
from .forms import notebookForm

# Create your views here.
def notebooksList(request):
    userInfo = navBarUserName(request)
    context = userInfo
    return render(request, 'notebooks/notebooksList.html', context)

import os
import subprocess
import time
from django_simfuel.views import navBarUserName
def notebooksView(request):
    userInfo = navBarUserName(request)
    if request.method == 'GET':
        subprocess.Popen(f'jupyter notebook static/notebooks/Test.ipynb --port 9000 --no-browser', shell=True)
        time.sleep(7)

    if request.method == 'POST':
        notes = request.POST.get('notesfield' or None)
        print(notes)
        subprocess.Popen('kill $(pgrep -f Test)', shell=True)
        return redirect('notebookList')
    context = userInfo
    return render(request, 'notebooks/notebooksView.html', context)

from django_simfuel.settings import UPLOAD_ROOT
def createNotebook(request):
    form = notebookForm()
    userInfo = navBarUserName(request)
    userId = request.user.id
    if request.method == 'POST':
        file = request.FILES['file']
        file_extension = os.path.splitext(file.name)[1]
        folderName = request.POST['name']
        print(file,file_extension,folderName)
        if not os.path.isdir(os.path.join(UPLOAD_ROOT, folderName)):
            os.mkdir(os.path.join(UPLOAD_ROOT, folderName))
        '''
        form = notebookForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():  
            form.save()
            return redirect('notebookList')
        '''
    context = {'form':form,
              }
    context = {**context, **userInfo}
    return render(request, 'notebooks/notebooksCreate.html', context)
