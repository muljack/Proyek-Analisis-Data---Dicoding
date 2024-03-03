import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

bike_day = pd.read_csv("dataset.csv")

st.header('Dashboard Data Persewaan Sepeda:sparkles:')
st.subheader('Berdasarkan Musim')

fig, ax = plt.subplots(figsize=(16, 8))

bike_day_season = bike_day.groupby(by=["year", "seasons"]).cnt.sum().reset_index()
sns.barplot(x=bike_day_season["seasons"], y=bike_day_season["cnt"], hue=bike_day_season['year'], palette='dark:blue')
plt.xlabel("Season")
plt.ylabel("Count")
plt.title("Jumlah Total Sewa Sepeda Berdasarkan Musim di Setiap Tahun", loc="center", fontsize=25)
st.pyplot(fig)

st.subheader('Berdasarkan Jenis Hari')
fig, ax = plt.subplots(figsize=(16, 8))

bike_day_typeofday = bike_day.groupby(by=["year", "typeofday"]).cnt.sum().reset_index()
sns.barplot(x=bike_day_typeofday["typeofday"], y=bike_day_typeofday["cnt"], hue=bike_day_typeofday['year'], palette='dark:blue')
plt.xlabel("Type of Day")
plt.ylabel("Count")
plt.title("Jumlah Total Sewa Sepeda Berdasarkan Jenis Hari di Setiap Tahun", loc="center", fontsize=25)
st.pyplot(fig)

st.subheader('Hubungan Jumlah Sepeda yang Disew dengan Suhu')
fig, ax = plt.subplots(figsize=(16, 8))

sns.scatterplot(data=bike_day, x="temp", y="cnt", hue="seasons", style="seasons", palette='dark')
plt.xlabel("Suhu (Celcius)")
plt.ylabel("Count")
plt.title("Hubungan Variabel Suhu dengan Variabel Jumlah Sepeda yang di Sewa ", loc="center", fontsize=25)
st.pyplot(fig)
