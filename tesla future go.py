#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install yfinance')
import yfinance as yf

tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")
tesla_data.reset_index(inplace=True)
tesla_data.head()


# In[7]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table", class_="historical_data_table")

dates = []
revenues = []

for row in table.tbody.find_all("tr"):
    cols = row.find_all("td")
    if len(cols) == 2:
        date = cols[0].text.strip()
        revenue = cols[1].text.strip().replace("$", "").replace(",", "")
        if revenue != "":
            dates.append(date)
            revenues.append(revenue)

tesla_revenue = pd.DataFrame({"Date": dates, "Revenue": revenues})
tesla_revenue["Revenue"] = pd.to_numeric(tesla_revenue["Revenue"])
tesla_revenue.tail()


# In[8]:


gme = yf.Ticker("GME")
gme_data = gme.history(period="max")
gme_data.reset_index(inplace=True)
gme_data.head()


# In[11]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")


table = soup.find("table", class_="historical_data_table")


dates = []
revenues = []

for row in table.tbody.find_all("tr"):
    cols = row.find_all("td")
    if len(cols) == 2:
        date = cols[0].text.strip()
        revenue = cols[1].text.strip().replace("$", "").replace(",", "")
        if revenue != "":
            dates.append(date)
            revenues.append(revenue)


gme_revenue = pd.DataFrame({"Date": dates, "Revenue": revenues})
gme_revenue["Revenue"] = pd.to_numeric(gme_revenue["Revenue"])
gme_revenue.tail()


# In[12]:


import plotly.graph_objs as go

def make_graph(stock_data, title):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=stock_data['Date'], y=stock_data['Close'], name='Stock Price'))
    fig.update_layout(title=title, xaxis_title='Date', yaxis_title='Price (USD)')
    fig.show()

make_graph(tesla_data, "Tesla Stock Price Over Time")


# In[13]:


make_graph(gme_data, "GameStop Stock Price Over Time")


# In[ ]:




