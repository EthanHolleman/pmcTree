import argparse

def get_args():
    parser = argparse.ArgumentParser('Create edgelists of PMC articles based on a specific articles citations.')
    parser.add_argument('root', metavar='R', help='PMCID of the root article to build the citation graph from.')
    parser.add_argument('outfile', metavar='O', help='Path to write edgelist to. Edgelist will have two columns. The first representing the "from" node and second representing the "to" node. Values are the PMC Ids of the articles without the "PMC" prefix.')
    parser.add_argument('-k', type=int, default=3, help='Max number of "layer" to explore. Default is 3 meaning from the root article the program will collect articles of citation distance away.')
    parser.add_argument('-till_complete', action='store_true', help='Continue building the article graph from the root until the entire citation network has been explored. No recommended as I have not actually seen this finish, just use a higher k value.')
    parser.add_argument('-backup_interval', default=1, help='How often to save a backup of the edgelist. Higher values will save less frequently. Recommended max = 3. The backup file will be the same format as the final output but named "backup.csv" and be saved in the working directory of the program.')
    return parser.parse_args()