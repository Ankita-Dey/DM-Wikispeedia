import csv, os
from math import log10, ceil

os.chdir(os.path.dirname(os.path.abspath(__file__)))

filepath = 'wikispeedia_paths-and-graph//categories.tsv'

with open(filepath, 'r') as f:
    categories = list(csv.reader(f, delimiter = '\t'))

categories = categories[13:]
s = set()
bfs = {0:['subject'], 1:s.copy(), 2:s.copy(), 3:s.copy()}

for category in categories:
    num_dots = category[1].count('.')
    bfs[num_dots].add(category[1])
    
    tmp = category[1][:category[1].rfind('.')]
    num_dots = tmp.count('.')
    while(num_dots >= 1):
        bfs[num_dots].add(tmp)
        tmp = tmp[:tmp.rfind('.')]
        num_dots = tmp.count('.')


for key in bfs.keys():
    bfs[key] = list(bfs[key])
    bfs[key].sort()

output = list()
count = 1
for i in [0,1,2,3]:
    for category in bfs[i]:
        id = 'C' + '0'*(4-ceil(log10(count+1))) + str(count)
        output.append([category, id])
        count+=1

output.sort()
output.insert(0, ['Category_Name', 'Category_Id'])

with open("category-ids.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(output)
