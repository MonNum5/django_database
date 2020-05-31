from django.shortcuts import render
# Create your views here.
from django_simfuel.views import navBarUserName
from datetime import datetime
from .forms import SearchForm
from .models import Search
from users.models import userModel
from databases.models import database
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def search(request):
    userInfo = navBarUserName(request)
    userId = request.user.id
    allowedDB = userModel.objects.get(user_id= userId).allowedDB

    
    objectList = []
    for db in allowedDB:
        try:
            databaseDescription = database.objects.get(dbAbbreviation= db)
            objectList.append(databaseDescription)
        except:
            pass
    
    form = SearchForm()
    if request.method == 'POST':
        form = request.POST
        #Trick django to allow the mutation of the query object
        mutable = request.POST._mutable #save non mutable status
        form._mutable = True    # set mutable to true
        # apply modifications
        form['user'] = userInfo['username'] # add user name that does the request
        form['selectedDB']=request.POST.get('selectedDbField', None) #add selected data bases
        # set back to non mutable status
        form._mutable = mutable
        # apply query set to form
        form = SearchForm(form)
        if form.is_valid(): # if valid process and save
            print(form.data)
            form.save()
            form = SearchForm()


            

    context = {'values':[
                {'id':1,'name':'fuel a','value':1,'fueltype':'NJFCP','project':'SAF','detail':{
                                                                                            'header':{
                                                                                                'id':1,
                                                                                                'name':'fuel a',
                                                                                                'fueltype':'NJFCP',
                                                                                                'project':'SAF'},
                                                                                            'properties':[
                                                                                                            {   
                                                                                                                "property":"flash_point",
                                                                                                                "test_method": "D93",
                                                                                                                "unit": "C",
                                                                                                                "value": 47.77777777777783
                                                                                                            },
                                                                                                            {                       "property":"freezing_point",
                                                                                                                "test_method": "D5972",
                                                                                                                "unit": "C",
                                                                                                                "value": -52.6
                                                                                                            },
                                                                                                            {   "property":"pour_point",
                                                                                                                "test_method": "D5949",
                                                                                                                "unit": "C",
                                                                                                                "value": -70.0
                                                                                                            }
                                                                                                        ]
                                                                                            
                                                                                            }
                
                },
                
                {'id':2,'name':'fuel b','value':1,'fueltype':'NJFCP','project':'SPK','detail':{
                                                                                            'header':{
                                                                                                'id':2,
                                                                                                'name':'fuel b',
                                                                                                'fueltype':'NJFCP',
                                                                                                'project':'SPK'},
                                                                                             'properties':[
                                                                                                            {   
                                                                                                                "property":"flash_point",
                                                                                                                "test_method": "D93",
                                                                                                                "unit": "C",
                                                                                                                "value": 60.77777777777783
                                                                                                            },
                                                                                                            {                       "property":"freezing_point",
                                                                                                                "test_method": "D5972",
                                                                                                                "unit": "C",
                                                                                                                "value": -90.6
                                                                                                            },
                                                                                                            {   "property":"pour_point",
                                                                                                                "test_method": "D5949",
                                                                                                                "unit": "C",
                                                                                                                "value": -30.0
                                                                                                            }
                                                                                                        ]
            
                                                                                            
                                                                                            }
                }
                ],
    'form':form
    }

    
    template_name = "search/search.html"
    context['dataBaseList']= objectList
    context ={**userInfo,**context}
    return (render(request, template_name, context))
