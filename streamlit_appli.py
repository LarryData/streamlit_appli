#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 15:54:58 2023

@author: macbook
"""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

st.title('Super Cars')
st.title("***")
st.title('Bienvenue')


link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_car = pd.read_csv(link)
selected_region = st.sidebar.selectbox("Select region", df_car["continent"].unique())
filtered_df_car = df_car[df_car["continent"] == selected_region]
st.write(filtered_df_car)


cor = df_car.corr()
correlation = plt.figure()
sns.heatmap(cor, center=0, vmin=-1, vmax=1,cmap="vlag", annot=True)
st.write(correlation)


fig = plt.figure()
sns.scatterplot(x="cylinders", y="time-to-60", data=df_car, hue="continent", color='red')
plt.suptitle("Puissance", size=12)
plt.ylabel("time-to-60")
plt.xlabel("cylinders")
plt.legend(title="continent", bbox_to_anchor=(1.0, 1.0), loc=1, borderaxespad=0, fontsize=8)
st.write(fig)

viz = plt.figure()
sns.violinplot(data = df_car,
               x = "continent",
               y = "cylinders",
               inner = "quartile")
st.write(viz)





