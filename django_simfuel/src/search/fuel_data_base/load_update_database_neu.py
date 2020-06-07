# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 11:32:42 2019

@author: hall_ce
Functions for loading data into database/ updating database, as well as
receiving data from database
"""

###############################################################################################################################    
# Update database content
import json
import os
from .database_helper_functions import list_files, get_keys_of_db, get_key_dict_check_similarity
from bson.objectid import ObjectId
import copy
import re
import numpy as np
from difflib import SequenceMatcher
import itertools

def update_db(db_name,folderpath,drop=False):
    db=db_name
    if drop==True:
        db.drop()
    json_files=list_files(folderpath,'json')
    a=0
    b=0
    for file in json_files:
        
        print(file)
        a+=1
        fuel_file = open(folderpath + file, 'r')
        parsed_file = json.loads(fuel_file.read())
        db.insert_one(parsed_file)

    print(str(a)+' files were succesfully loaded in database: '+str(db_name)+' '+str(b)+' files could not be loaded')
    
################################################################################################################################

#flatten direct results of query
def flatten(res):
    res_new = []
    props = [prop for prop in res.keys() if prop not in ['_id','name','project','fuel_type']]
    if props:
        for prop in props:
            for i in res[prop]:
                result_new = {
                            '_id': str(res['_id']),
                            'name': res['name'][0],
                            'project': res['project'][0],
                            'fuel_type': res['fuel_type'][0]
                            }
                result_new[prop] = i['value']
                for j in [k for k in i.keys() if k not in ['value']]:
                    result_new[j] = i[j]
                res_new.append(result_new)
    else:
        res_new = [{
                    '_id': str(res['_id']),
                    'name': res['name'][0],
                    'project': res['project'][0],
                    'fuel_type': res['fuel_type'][0]
                    }]
    return res_new

# flatten complete document
def flatten_doc(doc):
    doc_new = {}
    doc_new['header']=doc['header']
    #doc_new['change_log']=doc['change_log']
    change_list = []
    for i in doc['change_log']:
        change = {'Version':i}
        for key in ['Change','Timestamp','User']:
            try:
                change[key]=doc['change_log'][i][key]
            except:
                change[key]='-'
        change_list.append(change)
    doc_new['change_log'] = change_list
    for key in ['property','composition']:
        key_list = []
        for prop in doc[key].keys():
            if prop != 'GCxGC':
                try:
                    for i in doc[key][prop]:
                        i['property']=prop
                        key_list.append(i)
                except:
                    pass
        doc_new[key] = key_list
    return(doc_new)

#Get, Check and Process Data from Database

rex='\s*\_*\.*\-*\,*\;*' #ignore seperator for regex
def get_data_from_database(search_db,search_dict):
    
    keys_dict=get_keys_of_db(search_db)

    #Process Search_dict
    unwind_dict=[]
    match_dict_list=[]
    match_dict=[]
    unit_dict={}

    unwind_dict=[]
    pipeline=[]
    result_list=[]

    for item in search_dict:

        #Check correct input
        if type(item) != type({}):
           print(search_dict[item],' is not of type dict, please provide search item in search list [] in dict {} form')
           break
        if len(item)>2:
           print('Invalid input! Please provide input in form: {key:{constraint(s)},unit:(optional)},for each search item in the list []')
           break

        else:
            for d in item:

                label=get_key_dict_check_similarity(d,keys_dict)
                if label!=None:  #Check if label can be found     
                    if label not in match_dict_list: 
                        if type(item[d])==dict:
                            if 'unit' in item[d].keys():
                                unit_dict[label.split('.')[-1]]=item[d]['unit']
                        
                        unwind_dict.append('$'+label)
                        match_dict_dum=[]
                        if label=='_id': #search by file id
                            match_dict.append({'$match':item}) 
                        elif 'name' in label:
                                named=label.split('.')[-1]
                                if type(item[named])!=type([]):
                                    string=''
                                    for s in item[named]:
                                        if s==' ':
                                            continue
                                        else:
                                            string=string+s+rex
                                    name=re.compile(r'.*'+string+'.*',re.IGNORECASE)
                                    match_dict_dum={label:{'$regex':name}}
                                else:
                                    match_dict_dum2=[]    
                                    for j in item['name']:
                                        string=''
                                        for s in j:
                                            if s==' ':
                                                continue
                                            else:
                                                string=string+s+rex
                                        name=re.compile(r'.*'+string+'.*',re.IGNORECASE)
                                        match_dict_dum2.append({label:name})
                                    match_dict_dum={'$or':match_dict_dum2}
                                if len(match_dict_dum)>0:
                                    match_dict.append({'$match':match_dict_dum}) 
                        else:
                            for i in item[d]:  
                                try:
                                    if type(item[d][i])!=type([]):
                                        match_dict_dum={label+'.'+i:item[d][i]}
                                    else:
                                        match_dict_dum2=[]    
                                        for j in item[d][i]:
                                            match_dict_dum2.append({label+'.'+i:j})
                                        match_dict_dum={'$or':match_dict_dum2}
                                    if len(match_dict_dum)>0:
                                        match_dict.append({'$match':match_dict_dum}) 
                                except:
                                    if len(item[d])==1:
                                        match_dict_dum={label:i}
                                    else:
                                        match_dict_dum2=[]    
                                        for j in item[d]:
                                            match_dict_dum2.append({label:j})
                                        match_dict_dum={'$or':match_dict_dum2}
                                    if len(match_dict_dum)>0:
                                        match_dict.append({'$match':match_dict_dum}) 
                                    

                              
                        match_dict_list.append(label)
                        

                            
                        for i in unwind_dict:
                            pipeline.append({'$unwind':i})
                
                else:
                    print('no similar keyword could be found in database for search item: '+d)  
                    return([],[],[])
                
    pipeline=pipeline+match_dict
    group={'_id':'$_id','name':{'$addToSet':'$header.name'},'project':{'$addToSet':'$header.project'},'fuel_type':{'$addToSet':'$header.fuel_type'}}
    
    for d in match_dict_list: 
        if d!='_id':
            group[d.split('.')[-1]]={'$addToSet':'$'+d}
    
    pipeline.append({'$group':group})

    #databank search
    result=search_db.aggregate(pipeline)
    full_doc_dict = {}
    for res in result:
        res = res
        res = flatten(res)
        if res:
            result_list.append(res)
            doc = flatten_doc(search_db.find({"_id": ObjectId(res[0]["_id"])})[0])
            full_doc_dict[res[0]["_id"]] = doc

    return result_list, match_dict_list, unit_dict, full_doc_dict
     

def query_search_dict(process_dict, search_step_dict):
    '''
    process_dict={'Paper_Train':db.CRC_fuels}

    search_step_dict=[     
                  #[[{'density':{'unit':'kg/m3'}}],[{'viscosity_kinematic':{}}]],
                  [{'name':'crc'}]
                  ] 
    '''

    for step in search_step_dict:

        x_keys=[]
        y_keys=[]

        
        step_keys=[]
        
        #if [] in step, means desired correlations are defined
        if type(step[0])==list:

            search_dict=[]
            #append x labels
            for key in step[0]:
                x_keys.append(list(key.keys())[0])
                step_keys.append(list(key.keys())[0])
                search_dict.append(key)   
                
        
            #append y labels
            for key in step[1]:
                y_keys.append(list(key.keys())[0])
                search_dict.append(key)
                step_keys.append(list(key.keys())[0])
                
        #just data search
        else:
            search_dict=[]
            for key in step:
                search_dict.append(key)  
                step_keys.append(list(key.keys())[0])
        
        result_all = []
        doc_dict_all = {}
        for d in process_dict:
            result, match_dict_list, unit_dict, full_doc_dict =get_data_from_database(process_dict[d],search_dict)
            if result:
                result_all+=result
                doc_dict_all = {**doc_dict_all,**full_doc_dict}
        
        result_all = list(itertools.chain(*result_all))
    return result_all, doc_dict_all


from pymongo import MongoClient

def connect_to_db():
    #Call Database
    #client = MongoClient('localhost:27017') # defaults to port 27017
    ipv4='129.247.149.207'

    #New VM
    #superuser
    '''
    #superuser
    username="hall_ce"
    password="superstrongPwd"
    client = MongoClient("mongodb://" + username + ":" + password + "@"+ipv4+"/")
    db_aviation_fuel = client.aviation_fuel 
    db=db_aviation_fuel.all_fuel

    '''
    #docker container run as local host
    client=MongoClient('mongodb://localhost:27017/')

    db_aviation_fuel = client.aviation_fuel
    db=db_aviation_fuel.all_fuel
    return db
'''
db = connect_to_db()

process_dict={'CRC':db.CRC_fuels,'DLR fuels':db.OLD_JSON}

search_step_dict=[     
                #[[{'density':{'unit':'kg/m3'}}],[{'viscosity_kinematic':{}}]],
                [{'name':'crc'}]
                ] 

results, docs = query_search_dict(process_dict, search_step_dict)
'''

