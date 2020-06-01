from django.shortcuts import render, redirect

# Create your views here.
def notebooksList(request):
    return render(request, 'notebooks/notebooksList.html')

import os
import subprocess
import time
def notebooksView(request):
    #command = f'jupyter notebook {file_url} --port 9000'
    print(os.getcwd())
    #subprocess.run(f'jupyter notebook {file_url} --port 9000')
    #subprocess.call(f'jupyter notebook {file_url} --port 9000')
    subprocess.Popen(f'jupyter notebook static/notebooks/Test.ipynb --port 9000 --no-browser', shell=True)
    time.sleep(7)
    return render(request, 'notebooks/notebooksView.html')


def stopNotebook(request):
    subprocess.Popen('kill $(pgrep -f Test)', shell=True)
    return redirect('notebookList')