from django.shortcuts import render, redirect, get_object_or_404
from .forms import notebookForm
from .models import notebook
from django_simfuel.settings import MEDIA_ROOT
from shutil import copyfile
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required



import os
import subprocess
import time
from django_simfuel.views import navBarUserName

@staff_member_required()
def notebooksView(request, pk):
    userInfo = navBarUserName(request)
    obj = get_object_or_404(notebook, pk = pk)
    filename = obj.file.url.split('/')[-1]
    if request.method == 'GET':
        
        file_path = 'static'+obj.file.url
        subprocess.Popen(f'jupyter notebook {file_path} --port 9000 --no-browser', shell=True)
        time.sleep(7)

    if request.method == 'POST':
        notes = request.POST.get('notesfield' or None)
        print(notes)
        notebook.objects.filter(pk=pk).update(notes = notes)
        subprocess.Popen(f'kill $(pgrep -f {filename})', shell=True)
        return redirect('notebookList')

    context = {'notebook':obj, 'src':"http://localhost:9000/notebooks/"+filename}
    print(context)
    context = {**context, **userInfo}
    return render(request, 'notebooks/notebooksView.html', context)

@staff_member_required()
def createNotebook(request):
    form = notebookForm()
    userInfo = navBarUserName(request)
    userId = request.user.id
    
    context = {'form':form,
              }
    context = {**context, **userInfo}

    if request.method == 'POST':
        form = notebookForm(request.POST, request.FILES)
        try:
            file = request.FILES['file'] 
            file = request.FILES['file']       
            file_extension = os.path.splitext(file.name)[1]

            if file_extension != '.ipynb':
                context['error'] = 'Please provide a jupyter notebook in with a ipynb ending'
                context['form'] = form
                return render(request, 'notebooks/notebooksCreate.html', context)

        except:
            folderName = request.POST['name']
            if not os.path.isdir(os.path.join(MEDIA_ROOT, 'notebooks', folderName)):
                os.mkdir(os.path.join(MEDIA_ROOT, 'notebooks', folderName))
                copyfile(os.path.join(MEDIA_ROOT, 'notebooks', 'Test.ipynb'), os.path.join(MEDIA_ROOT, 'notebooks', folderName, 'Test.ipynb'))
            
        if form.is_valid():  
            form.save()
            return redirect('notebookList')
   
    
    return render(request, 'notebooks/notebooksCreate.html', context)


@login_required(login_url='login')
def notebooksList(request):
    userInfo = navBarUserName(request)
    userId = request.user.id

    obj = notebook.objects.all()

    context = {'notebooks':obj}
    context ={**userInfo,**context}
    return render(request, 'notebooks/notebooksList.html', context)


@staff_member_required()
def deleteNotebook(request, pk):
    obj = get_object_or_404(notebook, pk = pk)

    obj.delete()
    return redirect('notebookList')


@staff_member_required()
def updateNotebook(request, pk):
    obj = get_object_or_404(notebook, pk = pk)
    form = notebookForm(instance=obj)
    userInfo = navBarUserName(request)
    if request.method == 'POST':
        form = notebookForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("notebookList")
        
    context = {'form':form,
              }
    context = {**context, **userInfo}
    return render(request, 'notebooks/notebooksCreate.html', context)