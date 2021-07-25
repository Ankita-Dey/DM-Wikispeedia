import csv, os
import networkx as nx
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("edges.csv", 'r') as f:
    edgelist = list(csv.reader(f))

G = nx.DiGraph()
G.add_edges_from(edgelist[1:])


df = pd.read_csv('article-ids.csv')
articleid = df.set_index(['Article_Name']).to_dict(orient='dict')['Article_ID']

df = pd.read_csv('category-ids.csv')
categoryid = df.set_index(['Category_Name']).to_dict(orient='dict')['Category_Id']
idcategory = df.set_index(['Category_Id']).to_dict(orient='dict')['Category_Name']

df = pd.read_csv('article-categories.csv')
articlecat = df.set_index(['Article_ID']).to_dict(orient='dict')['Category_ID']

def pathlen(tmp):
    if len(tmp) > 1:
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
    return len(tmp)-1

def subcategories(categories):
    arr = []
    for category in categories:
        arr.append(category)

        tmp = idcategory[category]
        while(tmp.count('.') >= 1):
            tmp = tmp[:tmp.rfind('.')]
            arr.append(categoryid[tmp])
    return arr
    
def modifycatpair(src, des, srcarticle, desarticle, humanlen):
    for s in src:
        for d in des:
            try:
                shortlen = nx.shortest_path_length(G, srcarticle, desarticle)
              
                if shortlen == 0:
                    return
            except:
                return

            if (s,d) in catpair:
                catpair[(s,d)][0].append(humanlen)
                catpair[(s,d)][1].append(shortlen)
            else:
                catpair[(s,d)] = [[humanlen], [shortlen]]


catpair = dict()

filepath = 'wikispeedia_paths-and-graph//paths_finished.tsv'

with open(filepath, 'r') as f:
    finished = list(csv.reader(f, delimiter = '\t'))

for row in finished[16:]:

    tmp = row[3].split(';')
    categories = articlecat[articleid[tmp[0]]].split(',')
    src = subcategories(categories)       # if subcategories is required
    # src = categories                # if subcategories is not required
    
    categories = articlecat[articleid[tmp[-1]]].split(',')
    des = subcategories(categories)        # if subcategories is required
    # des = categories                  # if subcategories is not required

    modifycatpair(src, des, articleid[tmp[0]], articleid[tmp[-1]], pathlen(tmp))
    


output=[]
for key, val in catpair.items():
    row = list(key)
    # row.append(sum(val)/len(val))
    row.append(sum(val[0])/sum(val[1]))
    output.append(row)

output.sort()
output.insert(0, ['From_Category', 'To_Category', 'Ratio_of_human_to_shortest'])
with open("category-ratios.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(output)

