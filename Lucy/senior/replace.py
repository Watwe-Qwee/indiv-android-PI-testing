import pandas as pd

dataset = pd.read_csv('canvaLoadQState.csv')
def filter_function(dataframe):
    states=[]
    for index, row in dataset.iterrows():
        string = str(row[1])+str(row[2])
        if string not in states:
            states.append(string)
    return states

filtered_states = filter_function(dataset)
print("length :" + str(len(filtered_states)))
print("states :" + str(filtered_states))