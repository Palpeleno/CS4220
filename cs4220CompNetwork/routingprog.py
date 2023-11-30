class Node: 
    def __init__(self, node_id):
        self.node_id = node_id
        self.neighbors = {}
        self.routing_table = {}
    
    def add_neighbor(self,neighbor_id, cost):
        self.neighbors[neighbor_id] = cost
        
    def update_routing_table(self, destination, next_hop, path_cost):
        self.routing_table[destination] = {'next_hop':next_hop, 'path_cost':path_cost}
        
class Link:
    def __init__(self,source_node, destination_node, cost):
        self.source_node = source_node
        self.destination_node = destination_node
        self.cost = cost
class Topology:
    def __init__(self):
        self.nodes = {} #to store node
        self.links = [] #list to store links
    
    def add_node(self, node_id):
        self.nodes[node_id] = Node(node_id)
        
    def add_link(self, source_node, destination_node, cost):
        link = Link(source_node, destination_node, cost)
        self.links.append(link)
        self.nodes[nsource_nodeode1].add_neighbor(destination_node,cost)
        self.nodes[destination_node].add_neighbor(source_node,cost)
    
    def read_topology_file(self,file_path):
        with open (file_path, 'r') as file:
            for line in file:
                data = line.strip().split()
                source_node, destination_node, cost = map(int, data)
                self.add_node(source_node)
                self.add_node(destination_node)
                self.add_link(source_node, destination_node, cost)
                
                
        """
        Purpose: reads topo file line by line spliting them with
        source node, destintion node, and cost. first the file is 
        stripped line by line as the former parameters and maped 
        as a integer tripplet as in the file. nodes are apended  
        """
        
    # end def    
    def write_output_file(self, file_path):
        with open(file_path,'w') as file:
            #writes the forwarding tables from readable topofile
            for node_id in sorted(self.nodes):
                node = self.nodes[node_id]
                file.write(f"Forwarding Table for Node {node_id}:\n")
                for destination in sorted(node.routing_table):
                    entry = node.routing_table[destination]
                    file.write(f"{destination} {entry['next_hop']} {entry['path_cost']}\n")
        
 ## test driver functions        
topology = Topology()
topology.read_topology_file('topology.txt')
topology.write_output_file('output.txt')

# topology.add_node(1)
# topology.add_node(2)
# topology.add_link(1,2,3)

node1=topology.nodes[1]
print(f"Node ID: {node1.node_id}")
print(f"Neighbors: {node1.neighbors}")