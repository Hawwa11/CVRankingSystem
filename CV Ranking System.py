#!/usr/bin/env python
# coding: utf-8

# In[14]:


# Generate the database
# Import pandas library
import pandas as pd

# Read in data and display first 5 rows
df = pd.read_csv ('/Users/uSER/Downloads/CV.csv')

df


# In[15]:


# Calculate CV Score
# for each row of the data frame, get the name, age.. etc.

for index, row in df.iterrows():
    cvscore = 0
    
    #init
    cvscore = row["CV Score"]
    name = row["Name"]
    age = row["Age"]
    nationality = row["Nationality"]
    cgpa = row["CGPA"]
    qualification = row["Qualification Level"]
    yoe = row["Years of Experience"]
    

    #rule based stuff - do checking here
    #CGPA
    if cgpa >= 3.5:
        cvscore = cvscore + 6
    elif cgpa >= 2.5 and cgpa < 3.5:
        cvscore = cvscore + 4
    elif cgpa < 2.5:
        cvscore = cvscore + 1
        
    #AGE
    if age < 21:
        cvscore = cvscore + 3
    elif 21 <= age <= 40:
        cvscore = cvscore + 6
    elif age > 41 and age < 60:
        cvscore = cvscore + 1
        
    #YEARS OF EXPERIENCE
    if yoe == 0:
        cvscore = cvscore + 0
    elif 1 <= yoe <= 5:
        cvscore = cvscore + 4
    elif yoe > 5:
        cvscore = cvscore + 6
        
    #Qualification
    if qualification == "Pre-U":
        cvscore = cvscore + 1
    elif qualification == "Diploma":
        cvscore = cvscore + 2
    elif qualification == "Undergraduate":
        cvscore = cvscore + 3
    elif qualification == "Postgraduate":
        cvscore = cvscore + 4
            
    #finally add the CV score to the table
    df.at[index, "CV Score"] = cvscore

df


# In[16]:


# Sort df based on ranking of cv score
df = df.sort_values(by='CV Score', ascending=False,  na_position='last')

df


# In[ ]:




