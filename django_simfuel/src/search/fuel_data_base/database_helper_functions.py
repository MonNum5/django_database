# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 11:26:09 2019

@author: hall_ce

Description:
Helperfunctions for working with database

"""
import os
import copy
import numpy as np
from difflib import SequenceMatcher


#lists files given under path
def list_files(folder_path,ending):
    
    files=[]
    for file in os.listdir(folder_path):
    
        if file.endswith(ending):
            files.append(file)
    if not files:
        print('No files with the ending '+ending+' were found under the path '+folder_path)
    else:
        print(str(len(files))+' were found under the path '+folder_path)
    return(files)
    
def get_conversion_dict(c): #extra function due to simfuel database
    conversion_dict={'kg/m3':{'g/mL':1e-3*c,'g/cm3':1e-3*c},
                     'g/mL':{'kg/m3':1e3*c,'g/cm3':1*c},
                     'g/cm3':{'kg/m3':1e3*c,'g/mL':1*c},
                     'mN/m':{'dyne/cm':1*c,'dynes/cm':1*c},
                     'dyne/cm':{'mN/m':1*c,'dynes/cm':1*c},
                     'dynes/cm':{'mN/m':1*c,'dyne/cm':1*c},
                     'kJ/kg.K':{'J/gC':1*c,'J/gK':1*c,'kJ/(kg*K)':1*c},
                     'J/gC':{'kJ/kg.K':1*c,'J/gK':1*c,'kJ/(kg*K)':1*c},
                     'J/gK':{'J/gC':1*c,'kJ/kg.K':1*c,'kJ/(kg*K)':1*c},
                     'kJ/(kg*K)':{'J/gC':1*c,'kJ/kg.K':1*c,'J/gK':1*c},
                     'MJ/kg':{'kJ/kg':1000*c,'BTU/lb':429.923*c},
                     'kJ/kg':{'MJ/kg':1e-3*c,'BTU/lb':0.429923*c},
                     'BTU/lb':{'kJ/kg':2.326*c,'MJ/kg':0.002326*c},
                     'cSt':{'mm2/s':1*c},
                     'mm2/s':{'cSt':1*c},
                     'C':{'F':(c*9/5)+32,'K':c+273.15},
                     'F':{'C':(c-32)*5/9,'K':(c+459.67)*5/9},
                     'K':{'C':c-273.15,'F':(c*9/5)-459.67}}
    return(conversion_dict)
    
#Unit Converter
def convert_units(value_old,unit_old,unit_new):
    #convert units given in a conversion dict
    c=float(value_old)
    conversion_dict=get_conversion_dict(c)
    if unit_old!=unit_new:
        if unit_old not in conversion_dict:
            print('Unit: '+unit_old+' ought to be converted not in conversion table')
            value_new=value_old
        elif unit_new not in conversion_dict[unit_old]:
            print('Unit: '+unit_new+' ought to be converted to not in conversion table')
            value_new=value_old
        else:
            try:
                value_new=conversion_dict[unit_old][unit_new]
            except:
                return(print('Value: ',value_old,' not convertable to float'))
    else:
        value_new=float(value_old)
    return(value_new)

  
#Get keys of Database 
def get_keys_of_db(db,key_dict=['property','composition','header']):
    #Get keys of categories in database
    res_dict={}      
    for key in key_dict:
        result=db.aggregate([
          {"$project":{"arrayofkeyvalue":{"$objectToArray":'$'+key}}},
          {"$unwind":"$arrayofkeyvalue"},
          {"$group":{"_id":0,"allkeys":{"$addToSet":"$arrayofkeyvalue.k"}}}
        ])              
        for res in result:
            res_dict[key]=res['allkeys']
    return(res_dict)
  


def get_key_dict_check_similarity(key,keys_dict):
    #Find the key dict belonging (header,property,composition) and check the similartiy with keys like distillation_0%, density etc.
    matches={}
    for j,k in enumerate(keys_dict):
        if key=='_id':
            return('_id')
        if key in keys_dict[k]:
            return(k+'.'+key)
        elif j==len(keys_dict)-1:
            for j,k in enumerate(keys_dict):
                for val in keys_dict[k]:
                    sim=SequenceMatcher(None,key,val).ratio()
                    if sim>0.8:
                        matches[k+'.'+val]=sim
                if len(matches)>1:
                    print(key+' was not found literally in Database, similar keys are:', list(matches.keys()), ' Please provide more specefic input')
                    return(None)
      
                if len(matches)==1:
                    print(key+' was not found literally in Database,'+list(matches.keys())[0].split('.')[1]+' was chosen due to similarity')
                    return(list(matches.keys())[0])
    
                elif len(matches)==0:
                    print(key+' or similary key was not found in Database:')
                    return(None)
                    break

#Function to check for similarity of property file name and gcxgc file name 
def check_similarity_Property_GCxGC(key,keys_dict):
    #Find the key dict belonging (header,property,composition) and check the similartiy with keys like distillation_0%, density etc.
    matches={}
    
    if key in keys_dict:
        annot='-'
        return(key,annot)
    else:
        for val in keys_dict:
            sim=SequenceMatcher(None,key,val).ratio()
            if sim>0.9:
                matches[val]=sim
        if len(matches)>1:
            annot=key+' was not found literally in Database, similar keys are:', list(matches.keys()), ' Please provide more specefic input'
            print(annot)
            return(None,annot)
  
        if len(matches)==1:
            annot=key+' was not found literally in Database,'+list(matches.keys())[0]+' was chosen due to similarity'
            print(annot)
            return(list(matches.keys())[0],annot)

        elif len(matches)==0:
            annot=key+' or similary key was not found in Database:'
            print(annot)
            return(None,annot)
            
def check_outlier(values,unit):
    #detect and remove outlier in data 
    print_outlier=[]
    df=copy.deepcopy(values)
    mean=np.round(np.mean(df),3).values[0]
    std=np.round(np.std(df),3).values[0]
    for ind in list(df.index):
        
        if not abs(mean)-abs(3*std)<abs(df.loc[ind].values[0])<abs(3*std)+abs(mean):
           print('Outlier:{} {:.3f}[{}], mean: {:.3f} +/- {:.3f}[{}], for remove input rm'.format(ind,np.round(df.loc[ind].values[0],3),unit,mean,std,unit))           
           ipt=input()
           if ipt=='rm':
               values.drop(index=[ind],inplace=True)
               print('Outlier:{} {:.3f}[{}], mean: {:.3f} +/- {:.3f}[{}], removed'.format(ind,np.round(df.loc[ind].values[0],3),unit,mean,std,unit))
               print_outlier.append('Outlier:{} {:.3f}[{}], mean: {:.3f} +/- {:.3f}[{}], removed'.format(ind,np.round(df.loc[ind].values[0],3),unit,mean,std,unit))
           else:
               print('Outlier:{} {:.3f}[{}], mean: {:.3f} +/- {:.3f}[{}], NOT removed'.format(ind,np.round(df.loc[ind].values[0],3),unit,mean,std,unit))
               print_outlier.append('Outlier:{} {:.3f}[{}], mean: {:.3f} +/- {:.3f}[{}], NOT removed'.format(ind,np.round(df.loc[ind].values[0],3),unit,mean,std,unit))
        '''
        
        if not abs(mean)-abs(3*std)<abs(df.loc[ind].values[0])<abs(3*std)+abs(mean):
           print('Outlier:'+ind+':'+str(np.round(df.loc[ind].values[0],3))+'['+unit+'], mean:'+str(mean)+'+/-'+str(std)+'['+unit+'] for remove input rm')          
           ipt=input()
           if ipt=='rm':
               values.drop(index=[ind],inplace=True)
               print('Outlier:'+ind+':'+str(np.round(df.loc[ind].values[0],3))+'['+unit+'], mean:'+str(mean)+'+/-'+str(std)+'['+unit+'] removed')
               print_outlier.append('Outlier:'+ind+':'+str(np.round(df.loc[ind].values[0],3))+'['+unit+'], mean:'+str(mean)+'+/-'+str(std)+'['+unit+'] removed')
           else:
               print('Outlier:'+ind+':'+str(np.round(df.loc[ind].values[0],3))+'['+unit+'], mean:'+str(mean)+'+/-'+str(std)+'['+unit+'] NOT removed')
               print_outlier.append('Outlier:'+ind+':'+str(np.round(df.loc[ind].values[0],3))+'['+unit+'], mean:'+str(mean)+'+/-'+str(std)+'['+unit+'] NOT removed')
        ''' 
    return(values,print_outlier)
    
    
def write_ascii(GCxGC_file,Title,folderpath):
    #Save GCxGC File as ASCII format
    #Create Output Folder if new exist
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)
    print('Print ASCII-File {}'.format(Title))
    file = open(folderpath+"{}.dat".format(Title),"w")
    file.write('TITLE="{}"\n'.format(Title))
    file.write('VARIABLES="Carbon Number","Mass Fraction"\n')
    families={'n-alkane':'RED','iso-alkane':'BLUE','monocyclic-alkane':'GREEN','bicyclic-alkane':'GREEN','monocyclic-aromatics':'BLACK','naphtheno-aromatics':'GREEN','bicyclic-aromatics':'GREEN','alkenes':'blue'}
    for column in families.keys():
        file.write('ZONE T="{}", C=RED, I=25\n'.format(column))
        for i,value in enumerate(GCxGC_file[column]):
            file.write("\t\t{} {}\n".format(i,value))
    file.close()          
        