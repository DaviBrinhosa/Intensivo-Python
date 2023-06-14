#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Step 1: Import database
#Step 2: View the database
#Step 3: Handle the data - Incorrect format | Empty data
#Step 4: Initial analysis - Understand the client's note
#Step 5: Complete analysis - Find the ideal client profile

#!pip install openpyxl
#!pip install numpy
import plotly.express as px #!pip install plotly
import pandas as pd #!pip install pandas

#Step 1: 
table = pd.read_csv("client.csv", encoding="latin", sep=";")

#Step 2: 
#display(tabela)

#Step 3: 
table = table.drop("Unnamed: 8", axis=1) #axis=0 (Row) | axis=1 (Column)
#display(table)
#display(table.info())
table["Salário Anual (R$)"] = pd.to_numeric(table["Salário Anual (R$)"], errors="coerce")
table = table.dropna()

#Step 4: 
#display(table.describe())

#Step 5: 
#Create Graph
row = "Nota (1-100)"
#column = "Salário Anual (R$)"
for column in table.columns:
    if column != "Nota (1-100)":
        graph = px.histogram(table, x=column, y=row, histfunc="avg", text_auto=True, nbins=10)
        graph.show()

#View Graph
#Do an analysis and decide which parameters define the ideal client profile


# In[2]:


#Test Area

