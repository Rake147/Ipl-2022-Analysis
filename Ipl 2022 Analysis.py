#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# In[2]:


data=pd.read_csv("C:/Users/Rakesh/Datasets/IPL 2022.csv")


# In[3]:


data.head()


# In[4]:


figure=px.bar(data,x=data["match_winner"], title="Number of matches won in Ipl 2022")
figure.show()


# In[5]:


data["won_by"]=data["won_by"].map({"Wickets":"Chasing", "Runs":"Defending"})


# In[6]:


won_by=data["won_by"].value_counts()
label=won_by.index
counts=won_by.values
colors=['gold','lightgreen']


# In[7]:


fig=go.Figure(data=[go.Pie(labels=label,values=counts)])
fig.update_layout(title_text='Number of matches won by defending or chasing')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30, marker=dict(colors=colors,line=dict(color='black', width=3)))
fig.show()


# In[8]:


toss=data['toss_decision'].value_counts()
label=toss.index
counts=toss.values
colors=['skyblue','yellow']

fig=go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Toss Decision')
fig.update_traces(hoverinfo='label+percent',textinfo='value', textfont_size=30, marker=dict(colors=colors,line=dict(color='black',width=3)))
fig.show()


# In[9]:


# Top Scorers of IPL 2022
figure=px.bar(data,x=data['top_scorer'],title='Top scorers of ipl 2022')
figure.show()


# In[10]:


figure=px.bar(data,x=data['top_scorer'],y=data['highscore'],color=data['highscore'],title='Top scorers in IPL 2022')
figure.show()


# In[11]:


figure=px.bar(data,x=data['player_of_the_match'],title='Most player of the match awards')
figure.show()


# In[12]:


figure=px.bar(data,x=data['best_bowling'],title='Best Bowlers in Ipl 2022')
figure.show()


# In[13]:


#Most of the wickets fall in the first innings or second innings
figure=go.Figure()
figure.add_trace(go.Bar(x=data['venue'],y=data['first_ings_wkts'],name='First Innings Wickets',marker_color='gold'))
figure.add_trace(go.Bar(x=data['venue'],y=data['second_ings_wkts'],name='Second Innings Wickets',marker_color='lightgreen'))
figure.update_layout(barmode='group', xaxis_tickangle=-45)
figure.show()


# # Summary
# ### So this is how you can perform the task of IPL 2022 analysis using Python. IPL 2022 is going great for Gujrat as a new team this year. Jos Buttler and KL Rahul have been great with the bat, and Yuzvendra Chahal and Kuldeep Yadav have been great with the bowl.
