import py2neodriver
import gspreadcycle
import pickle

_pickle_filename = "pickle_tvshows"


nodes = None
headers = []

def __restore(filename):
    """
    __restore(filename): restores pickle file of Cell objects into "nodes" list.
    """
    with open(filename, 'rb') as file_object:
        raw_data = file_object.read()

    deserialized = pickle.loads(raw_data)
    file_object.close()
    global nodes
    nodes = deserialized
    for item in nodes:
        if item.header not in headers:
            headers.append(item.header)

def __graph(headers_list):
    DB = py2neodriver.db_init()
    graph = py2neodriver.graph_init()
    py2neodriver.graph_nodes(DB, graph, nodes, headers)
    py2neodriver.link_relations(DB, graph, nodes, headers)
        

def main():
    gspreadcycle.main()
    __restore(_pickle_filename)
    __graph(headers)

if __name__ == "__main__":
    main()
