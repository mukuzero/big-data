import pymongo as mg
from pymongo import MongoClient, UpdateOne, UpdateMany

import pandas as pd
from pandas import DataFrame
pd.set_option('display.max_columns', None)

import json
from datetime import datetime

#Creating a mongo client
myclient = mg.MongoClient("mongodb://localhost:27017/")
# <class 'pymongo.mongo_client.MongoClient'>

mydb    = myclient["repo"]
# <class 'pymongo.database.Database'>
mycol   = mydb["golden_repo"]
# <class 'pymongo.collection.Collection'>
mycol1  = mydb["guid_repo"]



mydb2   = myclient["master_repo"]
mycol2  = mydb2["master_collection"]

# Creating a pymongo cursor
cur = mycol1.find()
# <class 'pymongo.cursor.Cursor'>  # can be treated like list

# Converting Cursor object  into list
list_cur=list(cur)

# Creating a dataframe
guid_df=pd.DataFrame(list_cur)


# Getting the input file from the collection 

def getfilepath():

    # Passing keys domain_id  with value 1  & IBUCKETPATH with value 1   as argument in
    a = mycol2.find({},{'domain_id':1,'IBUCKETPATH':1})

    path = []
    for data in a:
        c = data['IBUCKETPATH']

        path.append(str(c))
 
        path1 = ' '.join(map(str, path))
        # print(path1)
        # print(type(path1))
        return path1
a=getfilepath()
 
def inputid(a):
    data=open(a,'r')
    input_df = pd.read_csv(data)
    # print(input_df)
    input_list = input_df['guid'].tolist()
    # print(input_list)
    golden_df = pd.DataFrame(list_cur)
    # print(golden_df)
    golden_list = golden_df['GUID'].tolist()
    # print(golden_list)
    c = [int(x) for x in golden_list]
    #Comparing two lists#
    merge_guid = []
    for i in input_list:
        if i in c:
            print('Matched records with GR which needs to be unmerged', (i))
            merge_guid.append(str(i))
        else:
            print('Records which doesnot match', (i))
    # print(type(merge_guid))
    # print(merge_guid)
    return merge_guid
# inputid(a)
# #
# #
# # # #Calling the input function with file as a parameter
# # # #file = "D:/Users/input/guid_unmerge.txt"
res=inputid(a)
# # print(res)
# # #
# # #
class unmerge:
    def __init__(self,ids):
        print(ids)
        self.ids=ids
        print(self.ids)

    #Function for adding the flag field  for the GUIDS unmerge
    def unmerge_golden(self):
        print("#################################")
        for item in self.ids:
            print("#########################################")
            print(item)
            filter, update = {"GUID": item}, {"$set": {"unmerge": "yes"}}
            mycol.update_many(filter, update)
            print("Unmerged Record {} Updated in Mongodb".format(item))

# Function for removing  the  indicator fields and updating them with respect to the unmergedGUID
    def unmerge_remove_ind_guid(self):
        # col_name = 'Consolidation_Ind'
        for item in self.ids:
            filter, update = {"GUID": item}, {'$unset': {'Consolidation_Ind': " "}}
            # db.testcollection.update_many({}, {"$unset": {f"{col_name}": 1}})
            mycol1.update_many(filter, update)
            # { $unset: {name: "", weight: ""}}
            print("Removed the consolidationindicatorof {} and Updated in Mongodb".format(item))

# Function for adding the OLD GUID fields and updating unmerged GUIDS
    def unmerge_guidrepo_update_oldguid(self):
        for item in self.ids:
            filter, update = {"GUID": item}, {"$set": {"OLDGUID": item}}
            mycol1.update_many(filter, update)
            print("Updated oldguid {} in Mongodb".format(item))
# Function for emptying the  GUID fields and updating them with respect to the unmergedGUID
    def unmerge_empty_guid(self):
        for item in self.ids:
            filter, update = {"GUID": item}, {"$set": {"GUID": " "}}
            mycol1.update_many(filter, update)
            print("Removed the oldguid {} and Updated in Mongodb".format(item))
def main():
    print(getfilepath())
    path = getfilepath()
    print(1)
    print(inputid(path))
    print(2)
    b = unmerge(inputid(path))
    b.unmerge_golden()
    b.unmerge_remove_ind_guid()
    b.unmerge_guidrepo_update_oldguid()
    b.unmerge_empty_guid()
main()