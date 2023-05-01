import pandas as pd
import streamlit as st

# Load the dataframe
pred_df = pd.read_csv('predictions.csv')

# Get a list of all the algorithms 
list_of_algorithms = ['Random Forest', 'Gradient Boosting', 'XGBoost', 'Linear Regression', 'Lasso', 'Ridge Regression', 'Elastic Net', 'k-NN', 'SVR']

# Get a list of all features' lists
list_of_features = ['All', 'All_without_G', 'Per36_with_AS', 'Totals_with_AS', 'Per36', 'AS']

# Create the Streamlit app
st.title("Predicting the NBA's MVP")
algorithm = st.selectbox('Select an algorithm', list_of_algorithms)
features = st.selectbox('Select a list of features', list_of_features)

# Sort the dataframe based on the selected algorithm and features
sorted_df = pred_df.sort_values(by=[algorithm + '_' + features, 'Player'], ascending=False)

# Remove original incides and add rankings
sorted_df = sorted_df.reset_index()
sorted_df['Rank'] = sorted_df.index + 1
sorted_df = sorted_df.set_index('Rank')

# Display the sorted dataframe
st.dataframe(sorted_df[['Player', algorithm + '_' + features]])