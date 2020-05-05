import pandas as pd 


random_list = [
    'Doug',
    'Lisa',
    'Megan',
    'Frank',
    'Sarah',
    'Trevor',
    'Tommy',
    'Bella'
]

data_frame = pd.DataFrame(random_list)


print(data_frame.isna())