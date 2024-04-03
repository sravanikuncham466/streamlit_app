import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
import math

st.title("Data App Assignment")

st.write("### Input Data and Examples")
df = pd.read_csv("Superstore_Sales_utf8.csv", parse_dates=True)
st.dataframe(df)

# This bar chart will not have solid bars--but lines--because the detail data is being graphed independently
st.bar_chart(df, x="Category", y="Sales")

# Now let's do the same graph where we do the aggregation first in Pandas... (this results in a chart with solid bars)
st.dataframe(df.groupby("Category").sum())
# Using as_index=False here preserves the Category as a column.  If we exclude that, Category would become the datafram index and we would need to use x=None to tell bar_chart to use the index
st.bar_chart(df.groupby("Category", as_index=False).sum(), x="Category", y="Sales", color="#04f")

# Aggregating by time
# Here we ensure Order_Date is in datetime format, then set is as an index to our dataframe
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df.set_index('Order_Date', inplace=True)
# Here the Grouper is using our newly set index to group by Month ('M')
sales_by_month = df.filter(items=['Sales']).groupby(pd.Grouper(freq='M')).sum()

st.dataframe(sales_by_month)

# Here the grouped months are the index and automatically used for the x axis
st.line_chart(sales_by_month, y="Sales")


category = st.selectbox("Select a Category", df['Category'].unique())
# (2) Add a multi-select for Sub_Category in the selected Category (1)
sub_categories = df[df['Category'] == category]['Sub_Category'].unique()
selected_sub_categories = st.multiselect("Select Sub-Category", sub_categories)
filtered_df=df[(df['Category']== category) & (df['Sub_Category'].isin(selected_sub_categories))]
# Initialize variables to avoid NameError
total_sales = 0
total_profit = 0
overall_profit_margin = 0
# (3) Show a line chart of sales for the selected items in (2)
if not filtered_df.empty:
    salesby_date = filtered_df.groupby('Order_Date')['Sales'].sum()
    st.line_chart(salesby_date)

# st.write("### (4) show three metrics (https://docs.streamlit.io/library/api-reference/data/st.metric) for the selected items in (2): total sales, total profit, and overall profit margin (%)")
# st.write("### (5) use the delta option in the overall profit margin metric to show the difference between the overall average profit margin (all products across all categories)")
