#!/usr/bin/env python
# coding: utf-8

# # Importar bibliotecas

# In[1]:


import pandas as pd


# # Leitura dos dados

# In[2]:


filename='./deputies_dataset.csv'
df=pd.read_csv(filename)
df.head(5)


# # Remover colunas desnecessárias

# In[4]:


df.drop(columns=['bugged_date', 'deputy_id', 'receipt_social_security_number', 'establishment_name'], inplace=True)
df.head(5)


# # Coletar o ano da coluna receipt_date

# In[5]:


# Listar tipo da coluna
df['receipt_date'].dtypes


# In[7]:


# Transformar coluna em data
df['receipt_date'] = pd.to_datetime(df['receipt_date'])
df.head(5)


# In[8]:


# Coletar o ano da coluna receipt_date
df['receipt_year'] = df['receipt_date'].dt.year
df.head(5)


# # Criar coluna de região

# In[10]:


# Criar nova coluna para receber os valores
df['region'] = 0
df.head(5)


# In[12]:


# Filtrar os campos de interesse e agregar a eles a região correta
df.loc[df['state_code'].isin(['SP', 'RJ', 'MG', 'ES']), 'region'] = 'Sudeste'
df.loc[df['state_code'].isin(['AC', 'RO', 'PA', 'AP', 'TO', 'AM', 'RR']), 'region'] = 'Norte'
df.loc[df['state_code'].isin(['MT', 'MS', 'GO']), 'region'] = 'Centro-Oeste'
df.loc[df['state_code'].isin(['MA', 'PI', 'CE', 'RN', 'PB', 'PE', 'AL', 'SE', 'BA']), 'region'] = 'Nordeste'
df.loc[df['state_code'].isin(['PR', 'SC', 'RS']), 'region'] = 'Sul'


# In[13]:


df.head(5)


# # Remover a coluna de receipt_date

# In[14]:


df.drop(columns=['receipt_date'], inplace=True)
df.head(5)

