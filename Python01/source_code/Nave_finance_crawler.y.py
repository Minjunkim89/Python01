#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[4]:


url = "https://finance.naver.com/item/main.nhn?code=005930"
result = requests.get(url)
bs_obj = BeautifulSoup(result.content, "html.parser")
bs_obj


# In[6]:


no_today = bs_obj.find("p", {"class":"no_today"})


# In[7]:


blind_now = no_today.find("span", {"class":"blind"})
blind_now


# In[9]:


blind_now.text


# In[ ]:




