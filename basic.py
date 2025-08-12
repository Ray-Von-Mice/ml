import pandas as pd
from datetime import datetime

# formatting output 3 digits after decimal
# pd.options.display.float_format = '{:.3f}'.format

input_file_path = '../input/melb_data.csv'
input_data = pd.read_csv(input_file_path)
input_data_desc = input_data.describe()

avg_lot_size = input_data_desc.iloc[1, input_data_desc.columns.get_loc('Landsize')]
print(avg_lot_size.round())
# print(input_data_desc.columns.tolist())

curr_year = datetime.now().year
newest_home_age = curr_year - input_data_desc.iloc[-1, input_data_desc.columns.get_loc('YearBuilt')]
print(newest_home_age)
