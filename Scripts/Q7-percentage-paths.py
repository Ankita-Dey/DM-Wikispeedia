import csv, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('finished-paths-no-back.csv', 'r') as f:
    pathsnoback = list(csv.reader(f))

with open('finished-paths-back.csv', 'r') as f:
    pathsback = list(csv.reader(f))

lennoback = [0 for i in range(12)] # path length 0, 1, 2 ... 10, >10
lenback = [0 for i in range(12)]

for i in range(1,len(pathsback)):
    try:
        if (int(pathsnoback[i][0]) - int(pathsnoback[i][1])) > 10:
            lennoback[11]+=1
        else:
            lennoback[int(pathsnoback[i][0]) - int(pathsnoback[i][1])]+=1

    except:
        print(pathsnoback[i])

    if (int(pathsback[i][0]) - int(pathsback[i][1])) > 10:
        lenback[11]+=1
    else:
        lenback[int(pathsback[i][0]) - int(pathsback[i][1])]+=1

sumnoback = sum(lennoback)
sumback = sum(lenback)

for i in range(len(lennoback)):
    lennoback[i] = lennoback[i]/sumnoback*100

for i in range(len(lenback)):
    lenback[i] = lenback[i]/sumback*100


output = [lennoback]
output.insert(0, ['Equal_Length','Larger_by_1','Larger_by_2','Larger_by_3','Larger_by_4','Larger_by_5','Larger_by_6','Larger_by_7','Larger_by_8','Larger_by_9','Larger_by_10','Larger_by_more_than_10'])

with open("percentage-paths-no-back.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(output)

output.clear()

output = [lenback]
output.insert(0, ['Equal_Length','Larger_by_1','Larger_by_2','Larger_by_3','Larger_by_4','Larger_by_5','Larger_by_6','Larger_by_7','Larger_by_8','Larger_by_9','Larger_by_10','Larger_by_more_than_10'])

with open("percentage-paths-back.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(output)
