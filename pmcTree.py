from pmcTree.article import expand_graph_from_root, write_edge_dict
from pmcTree.args import get_args


def main():
    args = get_args()
    edge_dict = expand_graph_from_root(args.root, k=args.k,
                                       till_complete=args.till_complete)
    write_edge_dict(args.outfile, edge_dict)


if __name__ == '__main__':
    main()
