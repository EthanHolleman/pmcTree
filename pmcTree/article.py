from pmcTree.api import get_cited_articles_from_pmc_id, parrell_citation_getter
import pprint
import pandas as pd
import sys
import csv

pp = pprint.PrettyPrinter(width=41, compact=True)
PMC_LINK_PREFIX = 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC{}'


def add_graph_layer(leaves, edge_dict, num_cpu=1):
    new_nodes = []
    response_dict = parrell_citation_getter(leaves, num_cpu)
    for each_id in leaves:
        if each_id not in edge_dict:
            cited_articles = get_cited_articles_from_pmc_id(each_id)
            if len(cited_articles) > 1:
                edge_dict[each_id] = cited_articles
                new_nodes += cited_articles

    return edge_dict, new_nodes

def test_graph_complete(leaves, edge_dict):
    complete = True
    for each_node in leaves:
        for each_cited_article in edge_dict[each_node]:
            if each_cited_article not in edge_dict:
                complete = False
                break
    return complete

def expand_graph_from_root(root_id, k=5, till_complete=False, backup_interval=1):
    edge_dict = {}
    root_citations = get_cited_articles_from_pmc_id(root_id)
    if len(root_citations) <= 1:
        print(f'PMC{root_id} either is not a valid ID or does not cite any articles')
        sys.exit()
    new_nodes = edge_dict[root_id]
    i = 0
    while True:
        if till_complete and not new_nodes:  # no nodes added
            break
        if not till_complete and i >= k:
            break
        if i % backup_interval == 0:
            write_edge_dict('backup_edgelist.csv', edge_dict)
        edge_dict, new_nodes = add_graph_layer(new_nodes, edge_dict)
        i += 1
    return edge_dict

def add_article_link_from_pmc_id(pmc_id):
    return PMC_LINK_PREFIX.format(pmc_id)

def convert_edge_dict_to_edge_list(edge_dict):
    edge_list = []
    for start_node in edge_dict:
        end_nodes = edge_dict[start_node]
        for end_node in end_nodes:
            edge = (start_node, end_node)
            edge_list.append(edge)

    return edge_list

def node_dict_from_edge_list(edge_list):
    all_nodes = set([])
    node_dict = {}
    for start, end in edge_list:
        all_nodes.add(start)
        all_nodes.add(end)
    for each_node in all_nodes:
        node_dict[each_node] = add_article_link_from_pmc_id(each_node)

def write_edge_dict(output_file, edge_dict):
    edge_list = convert_edge_dict_to_edge_list(edge_dict)
    with open(output_file, 'w') as handle:
        writer = csv.writer(handle)
        for edge in edge_list:
            writer.writerow(edge)
