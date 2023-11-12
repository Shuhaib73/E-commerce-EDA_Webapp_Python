import streamlit as st
import pandas as pd 

# Set up a title for the Streamlit app
st.markdown("<h1 style='text-align:center;'>Data Analysis Project</h1>", unsafe_allow_html=True)

# Read the sales and customer data CSV files

s_df = pd.read_csv('orders_2016-2020_Dataset.csv')
c_df = pd.read_csv('Customer_data.csv')


if 'number_of_rows' not in st.session_state:     # Initialize or retrieve the number of rows to be displayed in tables
    st.session_state['number_of_rows'] = 3


increment = st.number_input('Specify the number of rows to be displayed', 3,15)     # Allow the user to input the number of rows to be displayed
if increment:
    st.session_state['number_of_rows'] = increment


st.info('Sales Table')                                                              # Display sales and customer tables with specified number of rows
st.dataframe(s_df.head(st.session_state['number_of_rows']))
st.info('Customer Table')
st.dataframe(c_df.head(st.session_state['number_of_rows']))


st.info('Specify the Visualization to be displayed')                                # Allow the user to select a specific visualization
sl_btn = st.selectbox("Select", ['1. Analysis of Reviews given by Customers', '2. Analyzing the usage of various payment methods by customers', '3. Analyzing the top consumer states in India', '4. Analyze the distribution of top consumer Cities in India', '5. Analyzing the top-selling product categories', '6. Analyzing customer reviews across all product categories', '7. Analyzing the number of orders per year', '8. Analyzing the number of orders per Month', '9. Analyzing the number of orders per Day', '10. What is the breakdown of payment statuses for the canceled orders, showing the count of unpaid and paid statuses?'])

# Display the selected visualization based on user choice

if sl_btn == '1. Analysis of Reviews given by Customers':
    st.image('Visuals/Customer_Rating_oie.jpg')
elif sl_btn == '2. Analyzing the usage of various payment methods by customers':
    st.image('Visuals/Payment_dis_bar.jpg')
elif sl_btn == '3. Analyzing the top consumer states in India':
    st.image('Visuals/Top_customer_states.jpg')
elif sl_btn == '4. Analyze the distribution of top consumer Cities in India':
    st.image('Visuals/Top_cs_cities.jpg')
elif sl_btn == '5. Analyzing the top-selling product categories':
    st.image('Visuals/Top_Prd_barh.jpg')
elif sl_btn == '6. Analyzing customer reviews across all product categories':
    st.image('Visuals/Product_review_bar.jpg')
elif sl_btn == '7. Analyzing the number of orders per year':
    st.image('Visuals/Orders_year_br.jpg')
elif sl_btn == '8. Analyzing the number of orders per Month':
    st.image('Visuals/Order_month.jpg')
elif sl_btn == '9. Analyzing the number of orders per Day':
    st.image('Visuals/Order_day.jpg')
elif sl_btn == '10. What is the breakdown of payment statuses for the canceled orders, showing the count of unpaid and paid statuses?':
    st.image('Visuals/can_ord_st.jpg')


