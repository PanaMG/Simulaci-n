#!/usr/bin/env python
# coding: utf-8

# In[133]:


multiples3=[i*3 for i in range(1,101)]
print(multiples3)


# In[151]:


import pandas as pd
df=pd.read_excel("datosPE.xlsx")
imcs = [("imc de la persona" + str(i+1) + " es: " + str(df["Peso"][i]/(df["Estatura"][i]*df["Estatura"][i]))) for i in range(100)]
print(imcs)


# In[136]:


df


# In[153]:


import pandas as pd
df = pd.read_excel("datos.PE.xlsx")
imcs = [ df["Peso"][i]/(df["Estatura"][i]**2) for i in range(100)]

col = pd.DataFrame({"imc": imcs})

writer = ExcelWriter("datos.PE.xlsx")
col.to_excel(writer,'Sheet1',index=False)
writer.save()


# In[ ]:




