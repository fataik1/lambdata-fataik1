# my_lambdata assignment1.py

from pandas import DataFrame

def add_state_names(my_df):
    """
    Converts a dataframe with a comn of state abbreviations, adding a corrrsponding column of state

    Params: my_df a pandas.DataFrame with a column called ["abbrev"].
       example: DataFrame({"abbrev": ["CA", "CO","CT", "DC","TX"]}))
    """
    #State abbreviation -> Full Name and visa versa
   
    

    new_frame = my_df.copy()
        #Need a list or dict with the abbrev/name mappings
    names_map ={"CA":"Cali", "CO":"Colo",
         "CT":"Conn", "DC":"District of Columbia"}

        #Create a new column which maps the existing column using our names map
        #https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html
    #breakpoint()
        #type(type(new_frame['abbrev"])) #> <class 'pandas
        # dir(new_frame["abbrev"])
    new_frame["name"] = new_frame["abbrev"].map(names_map) 


    
    return new_frame
#State abbreviation -> Full Name and visa versa
if __name__ =="__main__":

   df = DataFrame({"abbrev":["CA", "CO", "CT", "DC", "TX"]})
   print(df.head())

   df2 = add_state_names(df)
   print(df2.head())