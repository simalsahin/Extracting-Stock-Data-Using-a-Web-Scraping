#!/usr/bin/env python
# coding: utf-8

# In[6]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html"
html_data = requests.get(url).text


# In[3]:


parse = BeautifulSoup(html_data,"html.parser")


# In[4]:


#title content
parse.title


# In[12]:


amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])
lst = []
for row in parse.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    amazon_data = amazon_data._append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)


# In[13]:


#Print out the first five rows of the amazon_data data frame you created.
amazon_data.head()


# In[14]:


#Question 2: What are the names of the columns in the data frame?
amazon_data.columns


# In[15]:


#Question 3: What is the Open of the last row of the amazon_data data frame?
amazon_data.tail(1)["Open"]


# In[ ]:




