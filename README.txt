
Either the .sh file for each of the assignment questions (from Q1 to Q11) is to be run in order, or the assign2.sh (of Q12) can be run on its own.

All output csv files are in the format given in assignment question.

All python scripts must have its dependencies in the same directory as the python script itself. wikispeedia_paths-and-graph folder must be present in the same directory as the python files.

The entire assignment took a maximum of 4 minutes to run in my computer.

Versions used:
python 3.7.9
pandas 1.1.1
csv 1.0
networkx 2.5


Q1:
Run in linux terminal:
python Q1-article-ids.py

Dependencies: 
Files: wikispeedia_paths-and-graph/articles.tsv
Python libraries: csv, os, math

Output: article-ids.csv

Time taken: Approximately 1 second


Q2:
Run in linux terminal:
python Q2-category-ids.py

Dependencies: 
Files: wikispeedia_paths-and-graph/categories.tsv
Python libraries: csv, os, math

Output: category-ids.csv

Time taken: Approximately 1 second


Q3:
Run in linux terminal:
python Q3-article-categories.py

Dependencies: 
Files: wikispeedia_paths-and-graph/categories.tsv, article-ids.csv, category-ids.csv
Python libraries: csv, os, pandas

Output: article-categories.csv

Time taken: Approximately 1 second


Q4:
NOTE: If a->b path length is 1 I have added edge a->b only and didn't assume b->a path to also be present unless found in shortest-path-distance-matrix.txt. Thus, edges can be considered as representing a directed graph (Can be used to construct undirected graph as well).

Run in linux terminal:
python Q4-edges.py

Dependencies: 
Files: wikispeedia_paths-and-graph/shortest-path-distance-matrix.txt
Python libraries: csv, os

Output: edges.csv

Time taken: Approximately 3-4 seconds


Q5:
NOTE: I have considered Undirected graph to find connected components

Run in linux terminal:
python Q5-graph-components.py

Dependencies: 
Files: edges.csv
Python libraries: csv, os, networkx

Output: graph-components.csv

Time taken: Approximately 2-3 seconds


Q6:
NOTE: If path a;b;<;c is given, I have considered with back as a->b->a->c and without back as a->c

Run in linux terminal:
python Q6-finished-paths.py

Dependencies: 
Files: wikispeedia_paths-and-graph/paths_finished.tsv, article-ids.csv, wikispeedia_paths-and-graph//shortest-path-distance-matrix.txt
Python libraries: csv, os, pandas

Output: finished-paths-no-back.csv, finished-paths-back.csv

Time taken: Approximately 6-7 seconds


Q7:
Run in linux terminal:
python Q7-percentage-paths.py

Dependencies: 
Files: finished-paths-no-back.csv, finished-paths-back.csv
Python libraries: csv, os

Output: percentage-paths-no-back.csv, percentage-paths-back.csv

Time taken: Approximately 1 second


Q8:
NOTE: I have considered directed graph to find shortest path since a->b path does not imply b->a path

Run in linux terminal:
python Q8-category-paths.py

Dependencies: 
Files: edges.csv, article-ids.csv, category-ids.csv, article-categories.csv, wikispeedia_paths-and-graph//paths_finished.tsv
Python libraries: csv, os, networkx, pandas

Output: category-paths.csv

Time taken: Approximately 5-6 seconds


Q9:
NOTE: I have considered directed graph to find shortest path since a->b path does not imply b->a path.

Run in linux terminal:
python Q9-category-subtree-paths.py

Dependencies: 
Files: edges.csv, article-ids.csv, category-ids.csv, article-categories.csv, wikispeedia_paths-and-graph//paths_finished.tsv
Python libraries: csv, os, networkx, pandas

Output: category-subtree-paths.csv

Time taken: Approximately 8-9 seconds


Q10:
Run in linux terminal:
python Q10-category-pairs.py

Dependencies: 
Files: edges.csv, article-ids.csv, category-ids.csv, article-categories.csv, wikispeedia_paths-and-graph//paths_finished.tsv, wikispeedia_paths-and-graph//paths_unfinished.tsv
Python libraries: csv, os, pandas

Output: category-pairs.csv

Time taken: Approximately 2-3 seconds


Q11:
NOTE: I have considered directed graph to find shortest path since a->b path does not imply b->a path. When multiple paths are there between a source destination pair, I have considred ratio as sum of all required human path lengths divided by all corresponding shortest path lengths.

Run in linux terminal:
python Q11-category-ratios.py

Dependencies: 
Files: edges.csv, article-ids.csv, category-ids.csv, article-categories.csv, wikispeedia_paths-and-graph//paths_finished.tsv
Python libraries: csv, os, networkx, pandas

Output: category-ratios.csv

Time taken: Approximately 40-50 seconds


Q12:
Run in linux terminal:
bash assign2.sh

Internally runs:
Q1-article-ids.py
Q2-category-ids.py
Q3-article-categories.py
Q4-edges.py
Q5-graph-components.py
Q6-finished-paths.py
Q7-percentage-paths.py
Q8-category-paths.py
Q9-category-subtree-paths.py
Q10-category-pairs.py
Q11-category-ratios.py

Dependencies:
Files: wikispeedia_paths-and-graph//articles.tsv, wikispeedia_paths-and-graph//categories.tsv, wikispeedia_paths-and-graph//paths_finished.tsv, wikispeedia_paths-and-graph//paths_unfinished.tsv, wikispeedia_paths-and-graph//shortest-path-distance-matrix.txt
Python libraries: pandas, csv, math, os, networkx

Output: article-ids.csv, category-ids.csv, article-categories.csv, edges.csv, graph-components.csv, finished-paths-no-back.csv, finished-paths-back.csv, percentage-paths-no-back.csv, percentage-paths-back.csv, category-paths.csv, category-subtree-paths.csv, category-pairs.csv, category-ratios.csv

Time taken: Approximately 4 minutes

