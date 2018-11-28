
# coding: utf-8

# In[150]:


import requests
import time
import json
import csv
from datetime import datetime, date, time, timedelta
import random


# In[151]:


def get_id_list_from_file(filename):
    with open(filename,'r') as file:
        id_list = json.load(file)
        
    return id_list


# In[152]:


sci_id_list = get_id_list_from_file('IDs_SCI.json')
mys_id_list = get_id_list_from_file('IDs_MYS.json')


# In[153]:


token = '988386c4311c0661e1fea9e2d88e3c3d69ba9f777819194dae8e5bb7b50579239850bece14d1a42bd613f&expires_in=86400&user_id=17159132'
link = 'https://oauth.vk.com/authorize?client_id=6306832&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends&response_type=token'


# In[154]:


def get_members_id_list(owner_id):    
    members_id_list =  []

    #first iteration for first 25k chunk
    try:
        r = requests.post('https://api.vk.com/method/execute.aa04201d?group_id='+
                          str(owner_id)+'&offset='+str(0)+'&count='+str(25000)+'&access_token='+token).json()['response']
    except KeyError as e:
        print(r)
        
    members_count = r[0] #number of total members
    
    print('Community: ', owner_id, ', members: ',members_count)
    
    members_id_list.extend(r[1]) #extend for a chunk of 25k
    
    if members_count > 25000:
        print('Community members > 25000. Starting loop..')
        for offset in range(25000, members_count, 25000):

            try:
                r = requests.post('https://api.vk.com/method/execute.aa04201d?group_id='+
                                  str(owner_id)+'&offset='+str(offset)+'&count='+str(25000)+'&access_token='+token).json()['response']
            except KeyError as e:
                print(r)
                
            members_id_list.extend(r[1])

            #t.sleep(.35)
        print('ID collected for community successfully: ')
    else:
        print('ID collected for community(<25k) successfully: ')

    return members_id_list


# In[155]:


def dump_all(foldername,id_list):
    
    for item in id_list:
        
        filename = foldername+'/'+item+'/'+'MEM_'+item+'.json'
        
        with open(filename,'w') as file:
            data = get_members_id_list(-int(item))
            json.dump(data,file,indent=2,ensure_ascii=False)
        
        file.close()


# In[156]:


dump_all('SCI',sci_id_list)

