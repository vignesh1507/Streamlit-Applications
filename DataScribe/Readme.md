# **DataScribe**

**DataScribe** is an interactive and intuitive tool designed to simplify the analysis and visualization of CSV data. Built using **Streamlit**, this tool allows users to upload CSV files, filter data, handle missing values, visualize correlations, and generate various plots. The processed data can also be downloaded in CSV format for further analysis.

## **Features**

1. **Data Upload:**
   - Upload any CSV file and instantly preview the first few rows of the data.
   
2. **Data Summary:**
   - View comprehensive statistics for both numeric and non-numeric columns, including count, mean, standard deviation, min/max values, and unique counts.

3. **Handle Missing Data:**
   - Drop rows with missing data or fill missing values with appropriate statistics:
     - Numeric columns are filled with the column mean.
     - Non-numeric columns are filled with the mode (most frequent value).

4. **Multi-Column Filtering:**
   - Filter the dataset based on specific column values. Easily explore data by selecting from available options.

5. **Correlation Heatmap:**
   - Visualize correlations between numeric columns using a heatmap, allowing quick insights into relationships within your dataset.

6. **Data Plotting:**
   - Generate various plots, including:
     - Line Chart
     - Bar Chart
     - Scatter Plot
     - Histogram
   - Choose any column as the x-axis and numeric columns as the y-axis.

7. **Download Processed Data:**
   - Download the filtered dataset in CSV format for offline analysis.

## **Installation**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/datascribe.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd datascribe
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app:**
   ```bash
   streamlit run main.py
   ```

## **Usage**

1. Upload a CSV file by clicking the **Choose a CSV file** button.
2. Preview the data and view summary statistics.
3. Handle missing data by dropping rows or filling missing values with appropriate statistics.
4. Filter the data based on specific columns and values.
5. Visualize correlations using a heatmap.
6. Generate and customize plots such as Line Charts, Bar Charts, Scatter Plots, and Histograms.
7. Download the filtered dataset in CSV format.

## **Contribution**

Feel free to fork this project, submit issues, and contribute improvements!

## **Credits**

**DataScribe** was developed using Python and Streamlit to create a user-friendly tool for CSV file analysis and visualization.
