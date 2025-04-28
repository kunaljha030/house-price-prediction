import pandas as pd
import pickle as pk
import streamlit as st


model = pk.load(open(r'E:\Project\House\House_prediction_model.pkl', 'rb'))
st.header('House Price Prediction')
data = pd.read_csv(r'E:\Project\House\bengaluru_house_prices.csv')

loc = st.selectbox('Choose the Location', data['location'].unique())
sqft = st.number_input('Enter the total square feet')
beds = st.number_input('Enter the number of bedrooms')
baths = st.number_input('Enter the number of bathrooms')
balc = st.number_input('Enter the number of balconies')


input = pd.DataFrame([[loc, sqft, beds,baths,balc]], 
                     columns=['location', 'total_sqft', 'bath', 'balcony', 'bedrooms'])

if st.button("Predict Price"):
   output = model.predict(input)
   out_str = 'Price of the House is: ' + str(output[0]*100000)
   st.success(out_str)