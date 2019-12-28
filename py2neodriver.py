from py2neo import Database, Graph, Node, Relationship
from gspreadcycle import GSpreadCycle


def db_init():
    DB = Database("bolt://localhost:7687")
    return DB

def graph_init():
    graph = Graph("bolt://localhost:7687", user="neo4j", password ="jenniferkwon")
    graph.delete_all()
    print("deleting previous graph is complete")
    return graph

def graph_nodes(DB, graph, nodes, headers):
    num_headers = len(headers)
    i = 0
    while i < (len(nodes) - num_headers):
        if nodes[i].content is not None and nodes[i+1].content is not None and nodes[i+2].content is not None and nodes[i+3].content is not None:
            a = Node(nodes[i].header, header = nodes[i].header, content = nodes[i].content, ID = nodes[i].ID)
            b = Node(nodes[i+1].header, header = nodes[i+1].header, content = nodes[i+1].content, ID = nodes[i+1].ID)
            c = Node(nodes[i+2].header, header = nodes[i+2].header, content = nodes[i+2].content, ID = nodes[i+2].ID)
            d = Node(nodes[i+3].header, header = nodes[i+3 ].header, content = nodes[i+3].content, ID = nodes[i+3].ID)
            graph.create(a)
            graph.create(b)
            graph.create(c)
            graph.create(d)
            if nodes[i+4].header == "Holiday" and nodes[i+4].content is not None:
                e = Node(nodes[i+4].header, holiday = nodes[i+4].content, ID = nodes[i+4].ID)
                graph.create(e)
                i+= 5
            else:
                i+= 4
                
def link_relations(DB, graph, nodes_list, headers): #more than one episode number and missing holiday in nodes_list?
    for index in range(len(nodes_list)):            #change Episode Number to lowercase
        if index == len(nodes_list) - 1:
            return
        if nodes_list[index].ID == nodes_list[index+1].ID:
            node_a_row = nodes_list[index].ID
            node_a_header = nodes_list[index].header
            node_a_content = nodes_list[index].content
            node_b_row = nodes_list[index+1].ID
            node_b_header = nodes_list[index+1].header
            node_b_content = nodes_list[index+1].content
            start_node = graph.nodes.match(str(node_a_header), ID = node_a_row, header = node_a_header).first()
            end_node = graph.nodes.match(str(node_b_header), ID = node_b_row, header = node_b_header).first()

            if node_a_header == "Holiday":
                print("found keyword")
            if start_node is not None and end_node is not None:
                graph.create(Relationship(start_node, node_b_header, end_node))
            
            #print(node_a_row, node_a_header, node_a_content)
            


"""
if __name__ == "__main__":
    db = Database("bolt://localhost:7687")

    graph = Graph("bolt://localhost:7687", user="neo4j", password ="jenniferkwon")
    graph.delete_all()
    print("deleting previous graph is complete")"""
