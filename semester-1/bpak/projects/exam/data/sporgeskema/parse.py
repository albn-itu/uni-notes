import pandas as pd 

data = pd.DataFrame(pd.read_csv("responses.csv", header=0))
columns = data.columns

for col in columns[1:25]:
    uni = []
    nun = []
    with open('out/' + col + ".txt", 'w') as filehandle:
        for row in data[col]:
            if (row not in uni):
                uni.append(row)
                nun.append(1)
            else:
                index = uni.index(row)
                nun[index] += 1
        
        for i in range(0, len(uni)):
            filehandle.write(str(nun[i]) + ' - ' + str(uni[i]) + '\n')