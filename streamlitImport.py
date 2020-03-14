import streamlit as st
import pandas as pd
import sqlite3
conn = sqlite3.connect("MSFT.db")
cursor = conn.cursor()
cursor.execute('SELECT * FROM stock_prices;')
records = cursor.fetchall()
df=pd.DataFrame(records, columns=['Row', 'Open','High','Low', 'Close','Date'])
df_prices=df.drop(['Row','Date'],axis=1)
st.line_chart(df_prices)
