#!/usr/bin/env python
# coding: utf-8

# In[4]:


FIRST CLASS 11/03
1. plot the data
2. build the model
3. run prior predictive checks
4. fit the model
5. evaluate convergence
6. run posterior checks
7. improve the model (-> 1)


# In[5]:


## PLOT THE DATA
    


# In[19]:


import pandas as pd
import matplotlib.pyplot as plt


# In[24]:


casos_covid = pd.read_csv('https://raw.githubusercontent.com/MinCiencia/'
                          'Datos-COVID19/master/output/producto5/TotalesNacionales_T.csv',
                         parse_dates= ['Fecha'])


# In[ ]:





# In[25]:


casos_covid.head()


# In[26]:


ax = casos_covid.plot('Fecha', 'Casos totales',
                     legend=False, figsize=(8,6))

