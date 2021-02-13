import requests
import re
import multiprocessing as mp
import time

#ARTICLES_THAT_CITE_URL = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?dbfrom=pubmed&linkname=pubmed_pmc_refs&id={}'
ARTICLES_CITED_URL = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?dbfrom=pmc&linkname=pmc_refs_pubmed&id={}'
pmc_id_regex = re.compile(r'<Id>(\d+)<\/Id>')

def get_cited_articles_from_pmc_id(pmc_id):
    response = requests.get(ARTICLES_CITED_URL.format(pmc_id))
    print(f'Accessing PMC{pmc_id} response: {response.status_code}')
    cites = set(pmc_id_regex.findall(str(response.content, 'utf-8')))
    if pmc_id in cites:
        cites.remove(pmc_id)
    return cites


def parrell_citation_getter(pmc_id_list, cpu_count=mp.Pool(mp.cpu_count())):
    pool = mp.Pool(cpu_count)
    results = pool.map(get_cited_articles_from_pmc_id, pmc_id_list)
    return dict(zip(pmc_id_list, results))

