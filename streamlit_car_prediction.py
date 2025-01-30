import streamlit as st
import pandas as pd
import plotly.express as px

#title
st.title("Data Visualization")

#upload csv
uploaded_file = st.file_uploader("Upload the file here", type=["csv", "xlsx"])

#check if the file has been uploaded
if uploaded_file is not None:
    #read the file into datafrae
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)

    #display first few rows
    st.subheader("Preview of the Dataset")
    st.write(df.head())

    #show basic statistics
    st.subheader("Basic Statistics")
    st.write(df.describe())
else:
    st.write("Please upload the correct file format")

#allow for viz
st.subheader("Visualization")

#select column for viz
if uploaded_file is not None:
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    categorical_columns = df.select_dtypes(include=['object']).columns

    #plot 1 histogram
    st.write("Histogram")
    selected_numerical_columns = st.selectbox("Select Numeric Columns", numeric_columns)
    if selected_numerical_columns:
        fig = px.histogram(df, x=selected_numerical_columns, title=f"Histogram of {selected_numerical_columns}")
        st.plotly_chart(fig)

    #plot 2 barplot
    st.write("Barplot")
    selected_categorical_columns = st.selectbox("Select Categorical Columns", categorical_columns)
    if selected_categorical_columns:
        fig = px.bar(df, x=selected_categorical_columns, title=f"Barplot of {selected_categorical_columns}")
        st.plotly_chart(fig)

    #plot 3 scatterplot
    st.write("Scatterplot")
    x_axis = st.selectbox("Select X-axis", numeric_columns)
    y_axis = st.selectbox("Select Y-axis", numeric_columns)
    color_column = st.selectbox("Select Color", categorical_columns)
    if x_axis and y_axis:
        fig = px.scatter(df, x=x_axis, y=y_axis, color=color_column ,title=f"Scatterplot of {x_axis} vs {y_axis}")
        st.plotly_chart(fig)
    
    #plot 4 correlation
    st.write("Correlation Heat Map")
    if st.checkbox("Generate Correlation Heatmap"):
        fig = px.imshow(df.corr())
        st.plotly_chart(fig)

    #plot 5 boxplot
    st.write("Boxplot")
    if st.checkbox("Generate Boxplot"):
        fig = px.box(df)
        st.plotly_chart(fig)