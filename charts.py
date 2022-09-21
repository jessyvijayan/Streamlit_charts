import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config( page_title= "Multipage app")
st.title("Main Page")

df = pd.read_excel('amazon_raw_data.xlsx')
df.drop(['Name'],axis=1,inplace=True)

## line chart
st.write("**This is a line chart**")
st.write('Please select the required axes')
x_axis = st.selectbox('Select required x-axis',('Performance','IQ','Motivation ','Annual Salary'),key=1)
y_axis = st.selectbox('Select required y-axis',('Performance','IQ','Motivation ','Annual Salary'),key=2)
if x_axis == 'Performance':
    if y_axis == 'Performance':
        st.error('Wrong option- Same axes!!')
    elif y_axis == 'IQ':
        st.line_chart(data=df,x='Performance',y='IQ')
    elif y_axis == 'Motivation ':
        st.line_chart(data=df,x='Performance',y='Motivation ')
    elif y_axis == 'Annual Salary':
        st.line_chart(data=df,x='Performance',y='Annual Salary')
elif x_axis == 'IQ':
    if y_axis == 'IQ':
        st.error('Wrong option- Same axes!!')
    elif y_axis == 'Performance':
        st.line_chart(data=df,x='IQ',y='Performance')
    elif y_axis == 'Motivation ':
        st.line_chart(data=df,x='IQ',y='Motivation ')
    elif y_axis == 'Annual Salary':
        st.line_chart(data=df,x='IQ',y='Annual Salary')
elif x_axis == 'Motivation ':
    if y_axis == 'Motivation ':
        st.error('Wrong option- Same axes!!')
    elif y_axis == 'Performance':
        st.line_chart(data=df,x='Motivation ',y='Performance')
    elif y_axis == 'IQ':
        st.line_chart(data=df,x='Motivation ',y='IQ')
    elif y_axis == 'Annual Salary':
        st.line_chart(data=df,x='Motivation ',y='Annual Salary')
elif x_axis == 'Annual Salary':
    if y_axis == 'Annual Salary':
        st.error('Wrong option- Same axes!!')
    elif y_axis == 'Performance':
        st.line_chart(data=df,x='Annual Salary',y='Performance')
    elif y_axis == 'IQ':
        st.line_chart(data=df,x='Annual Salary',y='IQ')
    elif y_axis == 'Motivation ':
        st.line_chart(data=df,x='Annual Salary',y='Motivation ')
else:
    st.write('Please choose an axis')

## area chart
st.write('**This is an area chart**')
st.write('Please select the required axes')
x_axis1 = st.selectbox('Select required x-axis',('Performance','IQ','Motivation ','Annual Salary'),key=3)
y_axis1 = st.selectbox('Select required y-axis',('Performance','IQ','Motivation ','Annual Salary'),key=4)
if x_axis1 == 'Performance':
    if y_axis1 == 'Performance':
        st.error('Wrong option- Same axes!!')
    elif y_axis1 == 'IQ':
        st.area_chart(data=df,x='Performance',y='IQ')
    elif y_axis1 == 'Motivation ':
        st.area_chart(data=df,x='Performance',y='Motivation ')
    elif y_axis1 == 'Annual Salary':
        st.area_chart(data=df,x='Performance',y='Annual Salary')
elif x_axis1 == 'IQ':
    if y_axis1 == 'IQ':
        st.error('Wrong option- Same axes!!')
    elif y_axis1 == 'Performance':
        st.area_chart(data=df,x='IQ',y='Performance')
    elif y_axis1 == 'Motivation ':
        st.area_chart(data=df,x='IQ',y='Motivation ')
    elif y_axis1 == 'Annual Salary':
        st.area_chart(data=df,x='IQ',y='Annual Salary')
elif x_axis1 == 'Motivation ':
    if y_axis1 == 'Motivation ':
        st.error('Wrong option- Same axes!!')
    elif y_axis1 == 'Performance':
        st.area_chart(data=df,x='Motivation ',y='Performance')
    elif y_axis1 == 'IQ':
        st.area_chart(data=df,x='Motivation ',y='IQ')
    elif y_axis1 == 'Annual Salary':
        st.area_chart(data=df,x='Motivation ',y='Annual Salary')
elif x_axis1 == 'Annual Salary':
    if y_axis1 == 'Annual Salary':
        st.error('Wrong option- Same axes!!')
    elif y_axis1 == 'Performance':
        st.area_chart(data=df,x='Annual Salary',y='Performance')
    elif y_axis1 == 'IQ':
        st.area_chart(data=df,x='Annual Salary',y='IQ')
    elif y_axis1 == 'Motivation ':
        st.area_chart(data=df,x='Annual Salary',y='Motivation ')
else:
    st.write('Please choose an axis')


## scatterplot
st.write('**This is an scatterplot**')
fig,ax = plt.subplots()
st.write('Please select the required axes')
x_axis2 = st.selectbox('Select required x-axis',('Performance','IQ','Motivation ','Annual Salary'),key=5)
y_axis2 = st.selectbox('Select required y-axis',('Performance','IQ','Motivation ','Annual Salary'),key=6)
if x_axis2 == 'Performance':
    if y_axis2 == 'Performance':
        st.error('Wrong option- Same axes!!')
    elif y_axis2 == 'IQ':
        ax = sns.scatterplot(data=df,x='Performance',y='IQ')
        st.pyplot(fig)
    elif y_axis2 == 'Motivation ':
        ax = sns.scatterplot(data=df,x='Performance',y='Motivation ')
        st.pyplot(fig)
    elif y_axis2 == 'Annual Salary':
        ax = sns.scatterplot(data=df,x='Performance',y='Annual Salary')
        st.pyplot(fig)
elif x_axis2 == 'IQ':
    if y_axis2 == 'IQ':
        st.error('Wrong option- Same axes!!')
    elif y_axis2 == 'Performance':
        ax = sns.scatterplot(data=df,x='IQ',y='Performance')
        st.pyplot(fig)
    elif y_axis2 == 'Motivation ':
        ax = sns.scatterplot(data=df,x='IQ',y='Motivation ')
        st.pyplot(fig)
    elif y_axis2 == 'Annual Salary':
        ax = sns.scatterplot(data=df,x='IQ',y='Annual Salary')
        st.pyplot(fig)
elif x_axis2 == 'Motivation ':
    if y_axis2 == 'Motivation ':
        st.error('Wrong option- Same axes!!')
    elif y_axis2 == 'Performance':
        ax = sns.scatterplot(data=df,x='Motivation ',y='Performance')
        st.pyplot(fig)
    elif y_axis2 == 'IQ':
        ax = sns.scatterplot(data=df,x='Motivation ',y='IQ')
        st.pyplot(fig)
    elif y_axis2 == 'Annual Salary':
        ax = sns.scatterplot(data=df,x='Motivation ',y='Annual Salary')
        st.pyplot(fig)
elif x_axis2 == 'Annual Salary':
    if y_axis2 == 'Annual Salary':
        st.error('Wrong option- Same axes!!')
    elif y_axis2 == 'Performance':
        ax = sns.scatterplot(data=df,x='Annual Salary',y='Performance')
        st.pyplot(fig)
    elif y_axis2 == 'IQ':
        ax = sns.scatterplot(data=df,x='Annual Salary',y='IQ')
        st.pyplot(fig)
    elif y_axis2 == 'Motivation ':
        ax = sns.scatterplot(data=df,x='Annual Salary',y='Motivation ')
        st.pyplot(fig)
else:
    st.write('Please choose an axis')

