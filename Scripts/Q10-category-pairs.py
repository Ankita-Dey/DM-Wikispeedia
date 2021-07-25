import csv, os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv('article-ids.csv')
articleid = df.set_index(['Article_Name']).to_dict(orient='dict')['Article_ID']

df = pd.read_csv('category-ids.csv')
categoryid = df.set_index(['Category_Name']).to_dict(orient='dict')['Category_Id']
idcategory = df.set_index(['Category_Id']).to_dict(orient='dict')['Category_Name']

df = pd.read_csv('article-categories.csv')
articlecat = df.set_index(['Article_ID']).to_dict(orient='dict')['Category_ID']


catpair = dict()

def subcategories(categories):
    arr = []
    for category in categories:
        arr.append(category)
        tmp = idcategory[category]

        while(tmp.count('.') >= 1):
            tmp = tmp[:tmp.rfind('.')]
            arr.append(categoryid[tmp])
    return list(set(arr))
    
def modifycatpair(src, des, n):
    for s in src:
        for d in des:
            if (s,d) in catpair:
                catpair[(s,d)][n]+=1
            else:
                tmp = [0,0]
                tmp[n] = 1
                catpair[(s,d)] = tmp


filepath = 'wikispeedia_paths-and-graph//paths_finished.tsv'

with open(filepath, 'r') as f:
    finished = list(csv.reader(f, delimiter = '\t'))

for row in finished[16:]:

    tmp = row[3].split(';')
    categories = articlecat[articleid[tmp[0]]].split(',')
    src = subcategories(categories)
    
    categories = articlecat[articleid[tmp[-1]]].split(',')
    des = subcategories(categories)
    
    modifycatpair(src, des, 0)
    

filepath = 'wikispeedia_paths-and-graph//paths_unfinished.tsv'

with open(filepath, 'r') as f:
    unfinished = list(csv.reader(f, delimiter = '\t'))

for row in unfinished[18:]:

    categories = articlecat[articleid[row[3].split(';')[0]]].split(',')
    src = subcategories(categories)
    
    try:
        des = subcategories(articlecat[articleid[row[4].split(';')[0]]].split(','))
    except:
        des = ['C0001']

    modifycatpair(src, des, 1)
    

output=[]
for key, val in catpair.items():
    row = list(key)
    row.append(val[0] / sum(val) * 100)
    row.append(val[1] / sum(val) * 100)
    output.append(row)

output.sort()
output.insert(0, ['From_Category', 'To_Category', 'Percentage_of_finished_paths', 'Percentage_of_unfinished_paths'])
with open("category-pairs.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(output)

