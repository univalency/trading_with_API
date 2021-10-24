
import pandas as pd



#Binance exports excel file, which I convert to csv
df = pd.read_excel('<your file>')


# In[3]:


#df = df.to_csv('<your file>')


# In[4]:


df = pd.read_csv('SOL_2021-10-24.csv')
df = df.values


# In[ ]:





# In[ ]:





# In[5]:


money_spent = 0
money_made = 0

coins_bought= 0
coins_sold = 0

buy_prices = []
sell_prices = []
fees = 0
orders = 0


# In[6]:


for j in range(174):
    if df[j][9] == 'Canceled':
        print(j)
        continue
        
    
    if df[j][3] == 'SELL':
        #print(float(df[j][4]))
        #print(float(df[j][5]))
        money_made += float(df[j][4]) * float(df[j][5])
        coins_sold += float(df[j][5])
        sell_prices.append(float(df[j][4]))
        orders += 1
            
    if df[j][3] == 'BUY':
        money_spent += float(df[j][4]) * float(df[j][5])
        buy_prices.append(float(df[j][4]))
        coins_bought += float(df[j][5])
        orders += 1
    
    #print (j)
    #print(df[j+2][5])


# In[ ]:





# In[8]:


#print(buy_prices)
print(money_spent)
print(money_made)
print(coins_bought)
print(coins_sold)
print(orders)
