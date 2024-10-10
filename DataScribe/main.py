import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("DataScribe")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Data Preview
    st.subheader("Data Preview")
    st.write(df.head())

    # Data Summary
    st.subheader("Data Summary")
    st.write(df.describe(include='all'))

    # Handling the Missing Data
    st.subheader("Missing Data")
    st.write(df.isnull().sum())

    if st.checkbox("Drop rows with missing data"):
        df = df.dropna()
        st.write(df)
    elif st.checkbox("Fill missing data with mean"):
        # Fill the numeric columns with mean
        numeric_cols = df.select_dtypes(include=['number']).columns
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

        # Fill the non-numeric columns with mode
        non_numeric_cols = df.select_dtypes(exclude=['number']).columns
        for col in non_numeric_cols:
            df[col].fillna(df[col].mode()[0], inplace=True)

        st.write(df)

    # Multi-Column Filtering
    st.subheader("Filter The Data")
    columns = df.columns.tolist()
    selected_columns = st.multiselect("Select columns to filter by", columns)

    if selected_columns:
        filters = {}
        for col in selected_columns:
            unique_values = df[col].unique()
            filters[col] = st.selectbox(f"Select value for {col}", unique_values)

        filtered_df = df.copy()
        for col, value in filters.items():
            filtered_df = filtered_df[filtered_df[col] == value]

        st.write(filtered_df)

    # Correlation Heatmap (only for numeric columns)
    if st.checkbox("Show Correlation Heatmap"):
        st.subheader("Correlation Heatmap")
        numeric_cols = df.select_dtypes(include=['number']).columns
        if len(numeric_cols) > 1:
            fig, ax = plt.subplots()
            sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', ax=ax)
            st.pyplot(fig)
        else:
            st.write("Not enough numeric columns to compute correlation.")

    # Data Plotting
    st.subheader("Plot Data")
    x_column = st.selectbox("Select x-axis column", columns)
    # Only allow numeric columns for y-axis
    y_column = st.selectbox("Select y-axis column", df.select_dtypes(include=['number']).columns)

    plot_type = st.selectbox("Select plot type", ["Line Chart", "Bar Chart", "Scatter Plot", "Histogram"])

    if st.button("Generate Plot"):
        fig, ax = plt.subplots()
        if plot_type == "Line Chart":
            st.line_chart(filtered_df.set_index(x_column)[y_column])
        elif plot_type == "Bar Chart":
            st.bar_chart(filtered_df.set_index(x_column)[y_column])
        elif plot_type == "Scatter Plot":
            ax.scatter(filtered_df[x_column], filtered_df[y_column])
            st.pyplot(fig)
        elif plot_type == "Histogram":
            st.write(f"Histogram of {x_column}")
            ax.hist(filtered_df[x_column], bins=20)
            st.pyplot(fig)

    # Download The Filtered CSV Data
    st.subheader("Download Data")
    if st.button("Download Filtered Data as CSV File"):
        csv = filtered_df.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="filtered_data.csv",
            mime="text/csv",
        )

else:
    st.write("Waiting on file upload...")
