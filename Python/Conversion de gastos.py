#!/usr/bin/env python
# coding: utf-8

# In[111]:


import pandas as pd
gastos_sin_editar = pd.read_csv('datasets/gastos/gastos.csv', sep=";", decimal = ",", dayfirst = True)
gastos2=gastos_sin_editar[["Fecha_Valor","Concepto","Importe"]]


# In[113]:


gastos2 = gastos2.rename(columns={"Fecha_Valor":"DATE", 
                        "Concepto":"CONCEPT", 
                        "Importe":"IMPORT"})
gastos2.loc[:,"OBSERVATION"] = 'NaN'


# In[114]:


mask = gastos2['IMPORT'] > 0
gastos2.loc[mask, 'CLASS'] = 'Income'
gastos2.loc[~mask, 'CLASS'] = 'Expense'


# In[115]:


mask = gastos2['CONCEPT'].str.lower().str.find('pepe mobil') >= 0
gastos2.loc[mask, 'TYPE'] = 'Phone'
gastos2.loc[mask, 'SUBTYPE'] = 'Pablo'


# In[ ]:


mask = gastos2['CONCEPT'].str.lower().str.find('yoigo') >= 0
gastos2.loc[mask, 'TYPE'] = 'Phone'
gastos2.loc[mask, 'SUBTYPE'] = 'Nilu'


# In[116]:


mask = gastos2['CONCEPT'].str.lower().str.find('consum') >= 0
gastos2.loc[mask, 'TYPE'] = 'Food'
gastos2.loc[mask, 'SUBTYPE'] = 'Groceries'


# In[117]:


mask = gastos2['CONCEPT'].str.lower().str.find('just') >= 0
gastos2.loc[mask, 'TYPE'] = 'Food'
gastos2.loc[mask, 'SUBTYPE'] = 'Delivery'


# In[ ]:


mask = gastos2['CONCEPT'].str.lower().str.find('dominos') >= 0
gastos2.loc[mask, 'TYPE'] = 'Food'
gastos2.loc[mask, 'SUBTYPE'] = 'Delivery'


# In[ ]:


mask = gastos2['CONCEPT'].str.lower().str.find('farmacia') >= 0
gastos2.loc[mask, 'TYPE'] = 'Pharmacy'


# In[ ]:


mask = gastos2['CONCEPT'].str.lower().str.find('ecooltra') >= 0
gastos2.loc[mask, 'TYPE'] = 'Movility'
gastos2.loc[mask, 'SUBTYPE'] = 'Motorbike'


# In[ ]:


mask = gastos2['CONCEPT'].str.lower().str.find('taxi') >= 0
gastos2.loc[mask, 'TYPE'] = 'Movility'
gastos2.loc[mask, 'SUBTYPE'] = 'Motorbike'


# In[ ]:


mask = gastos2['IMPORT'] = 675
gastos2.loc[mask, 'TYPE'] = 'Rental'


# In[110]:


gastos2.to_csv('datasets/Gastos/gastos_editado.csv', sep=";", decimal = ",", date_format = '%Y/%m/%d')


# In[ ]:




