#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[4]:


df = pd.DataFrame([1,3,5,7,9],index = ["A","B","C","D","E"])


# In[5]:


df


# In[13]:


data = {
   "Name": ["Gowtham","tanmai","sihi"],
    "age" : [20,21,2],
    "City":["Banglore","Mysore","hydrabad"]
}
df = pd.DataFrame(data)
df


# In[31]:


data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Mathematics': [85, 78, 92, 74],
    'Science': [88, 67, 90, 80],
    'English': [72, 83, 78, 85]
}
df = pd.DataFrame(data)

df["Average"]= df[["Mathematics","Science","English"]].mean(axis=1)

print(df)


# In[26]:


import pandas as pd

# Data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Mathematics': [85, 78, 92, 74],
    'Science': [88, 67, 90, 80],
    'English': [72, 83, 78, 85]
}

# Create the DataFrame
df = pd.DataFrame(data)

# Calculate the average marks for each student
df['Average'] = df[['Mathematics', 'Science', 'English']].mean(axis=1)

print(df)


# In[32]:


data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Mathematics': [85, 78, 92, 74],
    'Science': [88, 67, 90, 80],
    'English': [72, 83, 78, 85]
}
df = pd.DataFrame(data)

df["Average"] = df[["Mathematics","Science","English"]].median(axis=1)

df


# In[34]:


df["Average"] = df[["Mathematics","Science","English"]].mean(axis=1)
df


# In[44]:


data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Mathematics': [85, 78, 92, 74],
    'Science': [88, 67, 90, 80],
    'English': [72, 83, 78, 85]
}

df = pd.DataFrame(data)
df1 = df[df["Mathematics"]> 80]
df1


# In[53]:


data = {
    'A': [1, 2, None, 4, 5],
    'B': [5, None, 3, 8, None],
    'C': [10, 9, None, None, 7]
}
df = pd.DataFrame(data)
df1 = df.fillna(df.mean())
df1


# In[54]:


data = {
    'A': [1, 2, None, 4, 5],
    'B': [5, None, 3, 8, None],
    'C': [10, 9, None, None, 7]
}
df = pd.DataFrame(data)
df1 = df.fillna(df.mean())
df1


# In[56]:


df= pd.DataFrame(data)
df1 = df.fillna(df.mean())
df1


# In[11]:


import pandas as pd
data = {
    "name" : ["john","alice","bob"],
    "age" : [20,30,40],
    "city" : ["baglore","mysore","hyderabad"]    
}
df = pd.DataFrame(data)
df


# In[22]:


import pandas as pd

data1 = { 
    "Name": ["John", "Alice", "Bob"],  # Names should be in a list
    "age": [20, 23, 24],               # Ages should also be in a list
    "city": ["Bangalore", "Mysore", "Hyderabad"]  # Cities in a list
}

df = pd.DataFrame(data)
print(df)


# In[14]:


data = {
    "products" : ["shoes","socks","computers"],
    "price" : [20000,3000,230000],
    "quantity" : [10,20,30]
}
df = pd.DataFrame(data)
df


# In[17]:


data = {
    "names" : ["gautham","tanmai","sihi"],
    "grades" : ["B","A","F"],
    "subjects" : ["chemistry","maths","english"]
    
}
df = pd.DataFrame(data)
df


# In[20]:


df["grades"]


# In[21]:


df.grades


# In[23]:


data1


# In[26]:


data1["city"]


# In[31]:


data1["city"]


# In[59]:


data = {
    "Names" : ["Gautham","Tanmai","Sihi"],
    "age" : [29,26,np.nan],
    "city" : ["Banglore","Mysore","Hyderabad"]
}
df = pd.DataFrame(data)
df1 = df[["Names","city"]]
df1


# In[61]:


df.fillna(0,inplace = True)
df


# In[60]:


df["country"]="India","USA","japan"


# In[54]:


df[df["age"]>1]


# In[58]:


import pandas as pd
import numpy as np

data = {
    "Name": ["John", "Alice", "Bob"],
    "Age": [20, np.nan, 24],
    "City": ["Bangalore", np.nan, "Hyderabad"]
}

df = pd.DataFrame(data)
df.fillna(0,inplace = True)
df


# In[67]:


data = {
    "Names" : ["Gautham","Tanmai","Sihi"],
    "age" : [29,26,np.nan],
    "city" : ["Banglore","Mysore",np.nan]
}
df = pd.DataFrame(data)
df1 = df.dropna()
df1


# In[85]:


data = {
    "Names" : ["Gautham","Tanmai","Sihi"],
    "age" : [28,28,np.nan],
    "city" : ["Banglore","Mysore",np.nan]
}
df = pd.DataFrame(data)
df1 = df.rename(columns={"Names":"family members","city":"place"})
df1 = df.fillna(0,inplace = True)
df1


# In[88]:


df2 = df.sort_values(by = "age" , ascending = True)
df2


# In[90]:


df[df["age"]>20]
df


# In[93]:


df["city"]


# In[96]:


data = {
    "Names" : ["Gautham","Tanmai","Sihi"],
    "age" : [29,26,np.nan],
    "city" : ["Banglore","Mysore","Hyderabad"]
}
df = pd.DataFrame(data)
df1 = df[df["city"] == "Mysore"]
df1


# In[103]:


data = {
    "Name" : ["Gautham","tanmai","sihi"],
    "Age" : [20,21,5],
    "City" : ["Banglore","mysore","mysore"],
    "salary" : [35000,30000,0]
}
df = pd.DataFrame(data)
df


# In[104]:


df.head(2)


# In[106]:


df["department"] = ["HR","IT","finance"]
df


# In[110]:


df.pop("department")
df


# In[119]:


columns = df[["Name","salary"]]
columns


# In[126]:


data1 = df[df["salary"]>30000]
print(data1)


# In[132]:


columns = df.loc[(df["City"] == "Banglore") | (df["salary"]<30000)]
columns


# In[133]:


df


# In[137]:


df["Bonus"] = ["5000",np.NaN , "7000",]
df


# In[142]:


df["Bonus"] = df["Bonus"].fillna(3000)
df


# In[146]:


df1 = df.dropna()
df1


# In[151]:


df2 = df.groupby("City")["salary"].mean()
df2


# In[154]:


df.loc[df["Name"] == "sihi","salary"] = 20000
df


# In[157]:


df3 = df.groupby(["salary"]).median(numeric_only = True)
df3

