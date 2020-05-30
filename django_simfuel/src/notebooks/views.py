from django.shortcuts import render

# Create your views here.
def notebooksList(request):
    return render(request, 'notebooks/notebooksList.html')

def notebooksView(request):
    return render(request, 'notebooks/notebooks.html')


