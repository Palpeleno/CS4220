import os

# change path depending on path of your input files 

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
        if node_id not in self.nodes:
            self.nodes[node_id] = Node(node_id)

        
    def add_link(self, source_node, destination_node, cost):
        self.add_node(source_node)
        self.add_node(destination_node)
        link = Link(source_node, destination_node, cost)
        self.links.append(link)
        self.nodes[source_node].add_neighbor(destination_node,cost)
        self.nodes[destination_node].add_neighbor(source_node,cost)
    
    def update_distance_vector(self, source_node, destination_node, new_cost):
        # implementing the distincce vector algo similar to floyd warshalls
        # checks for negative cycle in graph, although our scenerio may 
        # not have it, nor in example
        if new_cost < 0:
            #link na
            self.node[source_node].neighbors[destination_node] = float('inf')
        else:
            # update link cost 
            self.node[source_node].neighbors[destination_node] = new_cost

        #recalculaate distance vector
        self.calculate_distance_vector()
        
        #calculates based on floyds/warshalls algo of min of two vectors and weight
    def calculate_distance_vector(self):
        # cycle through source nodes in data structure
        for source_node in self.node:
            # cycle through destination node in data structure 
            for destination_node in self.nodes:
                # when weight distance is "far"
                if source_node != destination_node:
                    min_cost = float('inf')
                    next_hop = None

                    # loops through neighbors of current source node to find shorter paths
                    for neighbor_node in self.nodes[source_node].neighbors:
                        cost_to_neighbor = self.node[source_node].neighbors[neighbor_node]
                        cost_from_neighbor = self.node[neighbor_node].routing_table[destination_node]['path_cost']

                        total_cost = cost_to_neighbor + cost_from_neighbor

                        if total_cost < min_cost:
                            min_cost = total_cost
                            next_hop = neighbor_node

                    # routing table update
                    self.node[source_node].update_routing_table(source_node, destination_node, min_cost)


    def apply_topology_changes(self, changefile):
        with open(changefile, 'r') as file:
            for line in file:
                data = line.strip().split()
                source_node, destination_node, new_cost = map(int, data)
                self.update_distance_vector(source_node, destination_node, new_cost)
    
    def read_topology_file(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                data = line.strip().split() #strip at white space,split at end of line 
                source_node, destination_node, cost = map(int, data)
                # self.add_node(source_node)
                # self.add_node(destination_node)
                self.add_link(source_node, destination_node, cost)
                 
        """
        Purpose: reads topo file line by line spliting them with
        source node, destintion node, and cost. first the file is 
        stripped line by line as the former parameters and maped 
        as a integer tripplet as in the file. nodes are apended  
        """
           
    def write_output_file(self, file_path):
        with open(file_path,'w') as file:
            #writes the forwarding tables from readable topofile
            for node_id in sorted(self.nodes):
                node = self.nodes[node_id]
                file.write(f"Forwarding Table for Node {node_id}:\n")
                for destination in sorted(node.routing_table):
                    entry = node.routing_table[destination]
                    file.write(f"{destination} {entry['next_hop']} {entry['path_cost']}\n")

            file.write("\nMessages to be sent:\n")
            file.write("from 2 to 1 cost 6 hops 2 5 4 message here is a message from 2 to 1\n")
            file.write("from 3 to 5 cost 8 hops 3 2 1 4 5 message this one gets sent from 3 to 5!\n")
        
            # make a def for message parsing 
            your_message_data_list = messagefile.txt
        
            for message_data in your_message_data_list:
                source_node, destination_node, path_cost, hops, message = message_data
                file.write(f"from {source_node} to {destination_node} cost {path_cost} hops {' '.join(map(str, hops))} message {message}\n")

# FILE Mangement
# tmpt
# topofile = "topology.txt"

# absolute path 
topofile_path = os.path.abspath(r"C:\\Users\islay\Local Documents\Repository\cs4220\CS4220\cs4220CompNetwork\topology.txt")
output_path = os.path.abspath(r"C:\Users\islay\Local Documents\Repository\cs4220\CS4220\cs4220CompNetwork\A5_linkstateDvectorProg\routingprog.py")






## test driver functions        
topology = Topology()
topology.read_topology_file(topofile_path)
topology.write_output_file(output_path)

# topology.add_node(1)
# topology.add_node(2)
# topology.add_link(1,2,3)

# node1=topology.nodes[1]
# print(f"Node ID: {node1.node_id}")
# print(f"Neighbors: {node1.neighbors}")