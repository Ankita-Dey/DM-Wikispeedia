import csv, os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv('article-ids.csv')
articleid = df.set_index(['Article_Name']).to_dict(orient='dict')['Article_ID']
articles = list(articleid.values())
articles.sort()

filepath = 'wikispeedia_paths-and-graph//paths_finished.tsv'

with open(filepath, 'r') as f:
    csv_reader = list(csv.reader(f, delimiter = '\t'))

csv_reader = csv_reader[16:]

pathsnoback = list()     # human path, path length without back
pathsback = list()     # human path, path length with back
reqpaths = dict()

for row in csv_reader:
    tmp = row[3].split(';')
    if len(tmp) > 1:
        reqpaths[(articleid[tmp[0]], articleid[tmp[-1]])] = None

        tmp2 = tmp.copy()
        i=0
        n = 1
        while(i<len(tmp2)-1):
            if tmp2[i+1] == '<':
                tmp2[i+1] = tmp2[i-n-1]
                n+=2
            else:
                n = 0
            i+=1
        pathsback.append([row[3], len(tmp2)-1])

        if '<' in tmp:
            i = 0
            while(i<len(tmp)-1):
                if tmp[i+1] == '<':
                    tmp.pop(i)
                    tmp.pop(i)
                    if tmp[i] == '<':
                        i-=1
                else:
                    i+=1
        
        pathsnoback.append([';'.join(tmp), len(tmp)-1])

i = 0   # tracks source in sortest distance txt
hp = 0 
with open('wikispeedia_paths-and-graph//shortest-path-distance-matrix.txt') as f:
    for line in f:
        if (line[0].isdigit() or line[0] == '_'):
            for j in range(len(articles)):
                if (articles[i], articles[j]) in reqpaths:
                    reqpaths[(articles[i], articles[j])] = line[j]
                    if line[j] == 0:
                        print(articles[i], articles[j])
            i+=1
            
i=0
while(i < len(pathsnoback)):
    tmp = pathsnoback[i][0].split(';')
    start = articleid[tmp[0]]
    end = articleid[tmp[-1]]

    pathsnoback[i].append(reqpaths[start, end])
    pathsback[i].append(reqpaths[start, end])

    if reqpaths[start, end] != '_' and int(reqpaths[start, end]) == 0:
            print(reqpaths[start, end],start, end)
            i+=1
        

    elif reqpaths[start, end] != '_':
        pathsnoback[i].append( pathsnoback[i][1] / int(reqpaths[start, end]))
        pathsback[i].append( pathsback[i][1] / int(reqpaths[start, end]))
        pathsnoback[i].pop(0)
        pathsback[i].pop(0)
        i+=1

    else:
        pathsnoback.pop(i)
        pathsback.pop(i)

pathsnoback.insert(0, ['Human_Path_Length', 'Shortest_Path_Length', 'Ratio'])

pathsback.insert(0, ['Human_Path_Length', 'Shortest_Path_Length', 'Ratio'])

with open("finished-paths-no-back.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(pathsnoback)

with open("finished-paths-back.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(pathsback)
