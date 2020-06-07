from django.shortcuts import render
# Create your views here.
from django_simfuel.views import navBarUserName
from datetime import datetime
from .forms import SearchForm
from .models import Search
from users.models import userModel
from databases.models import database
from django.contrib.auth.decorators import login_required
import json
from .fuel_data_base.load_update_database_neu import connect_to_db, query_search_dict
from django.core.serializers.json import DjangoJSONEncoder

db = connect_to_db()


@login_required(login_url='login')
def search(request):
    
    userInfo = navBarUserName(request)
    userId = request.user.id
    allowedDB = userModel.objects.get(user_id= userId).allowedDB
    
    objectList = []

    context = {}
    for db_i in allowedDB:
        try:
            databaseDescription = database.objects.get(dbAbbreviation= db_i)
            objectList.append(databaseDescription)
        except:
            pass
    
    form = SearchForm()
    context['form']=form
    if request.method == 'POST':
        
        CardId = list(request.POST.get('selectedDbCardIdField').split(','))

        form = request.POST
        #Trick django to allow the mutation of the query object
        mutable = request.POST._mutable #save non mutable status
        form._mutable = True    # set mutable to true
        # apply modifications
        form['user'] = userInfo['username'] # add user name that does the request
        selectedDb = request.POST.get('selectedDbField', None) #add selected data bases
        form['selectedDB']= selectedDb
        
        # set back to non mutable status
        form._mutable = mutable

        #set of query to fuel db
        process_dict = {}
        dbList = list(form['selectedDB'].split(','))

        if dbList[0]!='':

            for db_i in dbList:
                db_abb =database.objects.get(name = db_i)
                propdrop = request.POST.get('propertyField', None)
                search = request.POST.get('search', None)
                dum = 'db.'+db_abb.dbAbbreviation
                process_dict[str(db_i)] =  eval(dum)

                search_list = []
                if search != '' and search != None:
                    search_list.append({'name':search })
                if propdrop != '' and propdrop != None:
                    search_list.append({propdrop:{} })

            search_step_dict=[     
                        search_list
                        ] 

            results, docs = query_search_dict(process_dict, search_step_dict)
      
            context['values'] = json.dumps(results)
            context['detail'] = json.dumps([docs], cls=DjangoJSONEncoder)
            context['selectedDBlist'] = json.dumps(list(selectedDb.split(',')))
            context['CardId'] = json.dumps(CardId)
            
            # apply query set to form
            form = SearchForm(form)
            if form.is_valid(): # if valid process and save
                form.save()
                form = SearchForm()
        else:
        
            context['error']='Please select a collection'

    
    
    template_name = "search/search.html"
    context['dataBaseList']= objectList
    context ={**userInfo,**context}

    return (render(request, template_name, context))

