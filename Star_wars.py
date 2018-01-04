
# coding: utf-8

# In[8]:


import pandas as pd
star_wars = pd.read_csv("star_wars.csv", encoding="ISO-8859-1")


# In[2]:


star_wars.columns


# In[7]:


star_wars.head()


# In[16]:


star_wars = star_wars[star_wars['RespondentID'].notnull()]


# In[18]:


star_wars['RespondentID'].isnull().sum()


# In[20]:


cols = ['Have you seen any of the 6 films in the Star Wars franchise?',
       'Do you consider yourself to be a fan of the Star Wars film franchise?']

for c in cols:
    print(star_wars[c].value_counts())
    print(star_wars[c].isnull().sum())


# In[21]:


yes_no = {
    "Yes": True,
    "No": False
}

cols = ['Have you seen any of the 6 films in the Star Wars franchise?',
       'Do you consider yourself to be a fan of the Star Wars film franchise?']

for c in cols:
    star_wars[c] = star_wars[c].map(yes_no)


# In[22]:


star_wars.head()


# In[23]:


import numpy as np

movie_mapping = {
    "Star Wars: Episode I  The Phantom Menace": True,
    "Star Wars: Episode II  Attack of the Clones": True,
    "Star Wars: Episode III  Revenge of the Sith": True,
    "Star Wars: Episode IV  A New Hope": True,
    "Star Wars: Episode V The Empire Strikes Back": True,
    "Star Wars: Episode VI Return of the Jedi": True,
    np.nan: False
}

for col in star_wars.columns[3:9]:
    star_wars[col] = star_wars[col].map(movie_mapping)


# In[24]:


star_wars = star_wars.rename(columns={
        "Which of the following Star Wars films have you seen? Please select all that apply.": "seen_1",
        "Unnamed: 4": "seen_2",
        "Unnamed: 5": "seen_3",
        "Unnamed: 6": "seen_4",
        "Unnamed: 7": "seen_5",
        "Unnamed: 8": "seen_6"
        })

star_wars.head()


# In[26]:


star_wars = star_wars.rename(columns={
        "Please rank the Star Wars films in order of preference with 1 being your favorite film in the franchise and 6 being your least favorite film.": "ranking_1",
        "Unnamed: 10": "ranking_2",
        "Unnamed: 11": "ranking_3",
        "Unnamed: 12": "ranking_4",
        "Unnamed: 13": "ranking_5",
        "Unnamed: 14": "ranking_6"
        })


# In[31]:


cols = star_wars.columns[9:15]
star_wars[cols] = star_wars[cols].astype(float)


star_wars[cols].mean()


# In[29]:


star_wars[cols].head()


# In[30]:


import matplotlib.pyplot as plt


# In[39]:


plt.bar(range(6), star_wars[cols].mean())
plt.show()

# lower ranking is better
# In[40]:


star_wars[star_wars.columns[3:9]].sum()


# In[41]:


plt.bar(range(6), star_wars[star_wars.columns[3:9]].sum())
plt.show()


# In[42]:


males = star_wars[star_wars["Gender"] == "Male"]
females = star_wars[star_wars["Gender"] == "Female"]


# In[43]:


plt.bar(range(6), males[males.columns[9:15]].mean())
plt.show()

plt.bar(range(6), females[females.columns[9:15]].mean())
plt.show()

