import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
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

# st.write("## Your additions")
# st.write("### (1) add a drop down for Category (https://docs.streamlit.io/library/api-reference/widgets/st.selectbox)")

option = st.selectbox(
 'select category',
 ('Furniture', 'Office Supplies', 'Technology'))

st.write('You selected:', option)
li=[]
# st.write("### (2) add a multi-select for Sub_Category *in the selected Category (1)* (https://docs.streamlit.io/library/api-reference/widgets/st.multiselect)")
if option=='Furniture':
        options = st.multiselect(
           'Select Subcategory',
           ['Bookcases','Chairs','Furnishings','Tables']
       
)
elif option=="Office Supplies":
    options = st.multiselect(
    'Select Subcategory',
    ['Appliances','Art','Binders','Envelopes','Fasteners','Labels','Paper','Storage','Supplies']
)
else:
   options = st.multiselect(
   'Select Subcategory',
   ['Accessories','Copiers','Machines','Phones']
)
    

    

 # options = st.multiselect(
  #  'Select Subcategory',
 #   ['Accessories','Appliances','Art','Binders','Bookcases','Chairs','Copiers','Envelopes','Fasteners','Furnishings','Labels','Machines','Paper','Phones','Storage','Supplies','Tables']
# )

#st.write('You selected:', options)

# st.write("### (3) show a line chart of sales for the selected items in (2)")
#st.line_chart(df, x="options", y="Sales")

# Displaying a dropdown for category selection
#category = st.selectbox("Select Category", list(sub_categories.keys()))

# Retrieve sub-categories based on the selected category
#selected_sub_categories = st.multiselect("Select Sub-Category", sub_categories[category])

# Filter the DataFrame based on the selected sub-categories
#filtered_df = df[selected_sub_categories]

# Display line chart of sales for selected items
##st.write("### (3) Line Chart of Sales for Selected Items")
#st.line_chart(filtered_df)
# (2) Add a multi-select for Sub_Category in the selected Category (1)
sub_categories = df[df['Category'] == category]['Sub_Category'].unique()
selected_sub_categories = st.multiselect("Select Sub-Category", sub_categories)
# Initialize variables to avoid NameError
total_sales = 0
total_profit = 0
overall_profit_margin = 0
# (3) Show a line chart of sales for the selected items in (2)
if selected_sub_categories:
    mask = df['Sub_Category'].isin(selected_sub_categories)
    sales_by_month = df[mask].resample('M', on='Order_Date')['Sales'].sum()
    st.line_chart(sales_by_month)

st.line_chart(df.groupby("Sub_Category", as_index=False).sum(), x="Sub_Category", y="Sales", color="#04f")

# st.write("### (4) show three metrics (https://docs.streamlit.io/library/api-reference/data/st.metric) for the selected items in (2): total sales, total profit, and overall profit margin (%)")
# st.write("### (5) use the delta option in the overall profit margin metric to show the difference between the overall average profit margin (all products across all categories)")
