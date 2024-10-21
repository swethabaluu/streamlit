import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title and description
st.title("Simple Data Visualization App")
st.write("Upload your dataset in CSV format to visualize data with bar and line charts.")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)
    
    # Display the dataframe
    st.subheader("Data Preview")
    st.dataframe(df.head())

    # Column selection for visualization
    columns = df.columns.tolist()
    st.subheader("Select columns for visualization")
    x_axis = st.selectbox("Select X-axis", columns)
    y_axis = st.selectbox("Select Y-axis", columns)

    # Bar chart
    st.subheader("Bar Chart")
    if st.button("Generate Bar Chart"):
        fig, ax = plt.subplots()
        df.plot(kind="bar", x=x_axis, y=y_axis, ax=ax)
        st.pyplot(fig)

    # Line chart
    st.subheader("Line Chart")
    if st.button("Generate Line Chart"):
        fig, ax = plt.subplots()
        df.plot(kind="line", x=x_axis, y=y_axis, ax=ax)
        st.pyplot(fig)

else:
    st.write("Please upload a CSV file to visualize data.")
