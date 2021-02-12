# pmcTree
Python command line program for creating edgelists (and graphs) from a PMC article's citations.

# Usage

```
python pmcTree.py
usage: Create edgelists of PMC articles based on a specific articles citations.
       [-h] [-k K] [-till_complete] [-backup_interval BACKUP_INTERVAL] R O

positional arguments:
  R                     PMCID of the root article to build the citation graph from.
  O                     Path to write edgelist to. Edgelist will have two columns. The first
                        representing the "from" node and second representing the "to" node.
                        Values are the PMC Ids of the articles without the "PMC" prefix.

optional arguments:
  -h, --help            show this help message and exit
  -k K                  Max number of "layer" to explore. Default is 3 meaning from the root
                        article the program will collect articles of citation distance away.
  -till_complete        Continue building the article graph from the root until the entire
                        citation network has been explored. No recommended as I have not
                        actually seen this finish, just use a higher k value.
  -backup_interval BACKUP_INTERVAL
                        How often to save a backup of the edgelist. Higher values will save less
                        frequently. Recommended max = 3. The backup file will be the same format
                        as the final output but named "backup.csv" and be saved in the working
                        directory of the program.
 ```
 
 # Output format
 
 Edgelists are output as 2 column csv files of the numeric portion of article PMC Ids. Edges are directed in the sense
 that the article specified by the node in the first column of the edge list cites the articles specified
 in the second column. 
 
 A small example is below
 
 ```
 4423606,4423606
4423606,24091329
.
.
.
4423606,23386393
4423606,23336100
```
You could access an article by filling in the `{}` in `https://www.ncbi.nlm.nih.gov/pmc/articles/PMC{}` with the values of the edgelist.
                       
