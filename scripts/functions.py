from pandas import DataFrame,Series

def str_to_list(df:DataFrame,column_name:str):
    new_column=[]
    for value in df[column_name].values:
        values_as_list = str(value).split(",")
        values_as_list = [element.strip() for element in values_as_list]
        new_column.append(values_as_list)
    df[column_name] = new_column
    return df

def flatten(list_of_lists:Series):
    flattened_list = [str(element).strip() for single_list in list_of_lists for element in single_list]
    return Series(flattened_list)