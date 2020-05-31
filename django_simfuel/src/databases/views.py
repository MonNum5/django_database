from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required

from .forms import dataBaseForm, dataBaseFormUpdate
from django_simfuel.views import navBarUserName
from users.models import userModel
from databases.models import database
from django.contrib.auth.decorators import login_required

@staff_member_required()
def registerDB(request):
    form = dataBaseForm()
    userInfo = navBarUserName(request)
    userId = request.user.id
    if request.method == 'POST':
        form = dataBaseForm(request.POST)
        if form.is_valid():  
            allowedDB = userModel.objects.get(user_id= userId).allowedDB
            allowedDB.append(form.cleaned_data['dbAbbreviation'])
            userModel.objects.filter(user_id= userId).update(allowedDB = allowedDB)
            form.save()
            return redirect("listDB")
    context = {'form':form,
              }
    context = {**context, **userInfo}
    return render(request, 'databases/registerDB.html', context)

@staff_member_required()
def updateDB(request, pk):
    obj = get_object_or_404(database, pk = pk)
    form = dataBaseFormUpdate(instance=obj)
    userInfo = navBarUserName(request)
    if request.method == 'POST':
        form = dataBaseFormUpdate(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("listDB")
        
    context = {'form':form,
              }
    context = {**context, **userInfo}
    return render(request, 'databases/registerDB.html', context)

@staff_member_required()
def deleteDB(request, pk):
    obj = get_object_or_404(database, pk = pk)
    userId = request.user.id
    dbAbbreviation = obj.dbAbbreviation
    allowedDB=userModel.objects.get(user_id= userId)
    new_list = [i for i in allowedDB.__dict__['allowedDB'] if i != dbAbbreviation]
    userModel.objects.filter(user_id= userId).update(allowedDB = new_list)

    obj.delete()


    return redirect("listDB")

@login_required(login_url='login')
def listCollections(request):
    userInfo = navBarUserName(request)

    userId = request.user.id
    allowedDB = userModel.objects.get(user_id= userId).allowedDB
    registerForm = dataBaseForm()
    objectList = []
    for db in allowedDB:
        try:
            databaseDescription = database.objects.get(dbAbbreviation= db)
            objectList.append(databaseDescription)
        except:
            pass

    context = {'registerForm':registerForm, 'dataBaseList':objectList}
    context ={**userInfo,**context}
    return (render(request, 'databases/listDB.html', context))