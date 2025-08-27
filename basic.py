import pandas as pd
from datetime import datetime
from sklearn.tree import DecisionTreeRegressor

# formatting output 3 digits after decimal
# pd.options.display.float_format = '{:.3f}'.format

input_file_path = '../input/melb_data.csv'
input_data = pd.read_csv(input_file_path)
# input_data_desc = input_data.describe()

# # extract average lot size
# avg_lot_size = input_data_desc.iloc[1, input_data_desc.columns.get_loc('Landsize')]
# print(avg_lot_size.round())
# 
# # calculate newest home age by substracting current year with newest home built year
# curr_year = datetime.now().year
# newest_home_age = curr_year - input_data_desc.iloc[-1, input_data_desc.columns.get_loc('YearBuilt')]
# print(newest_home_age)
 
# print(input_data.columns)

# dropna drops missing values (think of na as "not available")
melbourne_data = input_data.dropna(axis=0)
y = melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
x = melbourne_data[melbourne_features]

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)
melbourne_model.fit(x, y)
print("Making predictions for the following 5 houses:")
print(x.head())
print("The predictions are")
print(melbourne_model.predict(x.head()))
