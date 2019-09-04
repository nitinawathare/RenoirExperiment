class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    def add_edge(self, src, dest):
        # Adding the node to the source node
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

    # Function to print the graph
    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


def dependency(s, total):
    for i, e in reversed(list(enumerate(total))):
        for j in s:
            if j in e:
                return i
    return 'nan'


if __name__ == "__main__":
    count = 0
    txdict = {}
    sload = []
    sstore = []
    total_store = []
    check = 0
    indexdata = []
    contract = 0
    file = "/home/shashi/renoir_exp/block/8433696"
    with open(file, 'r') as f:
        line = list(f)[-1]
        lastline = line.split(',')
        txcount = lastline[1]
        f.close()
        V = int(txcount)
        graph = Graph(V)
    with open(file, 'r') as f:
        for linedata in f:
            data = linedata.split(',')
            if data[0] == "hash:":
                count = count + 1
                if check == 0:
                 check = 1
                 checklast = "hash"
                elif check == 1:
                    if checklast != "hash":
                        contract = contract+1
                    a = sload[:]
                    b = sstore[:]
                    txdict[count] = data[1]
                    index = dependency(a, total_store)
                    if index != 'nan':
                        graph.add_edge(index, count)
                    indexdata.append(index)
                    total_store.append(b)
                    sstore.clear()
                    sload.clear()
                    checklast="hash"
            elif data[0] == "SLOAD:":
                sload.append(data[1])
                checklast = "sload"
            elif data[0] == "SSTORE:":
                sstore.append(data[1])
                checklast = "sstore"
    a = sload[:]
    index = dependency(a, total_store)
    if index != 'nan':
        graph.add_edge(index, count)
    indexdata.append(index)
    tx = 0
    print(indexdata)
    for k in indexdata:
        if k != 'nan':
            tx = tx+1
    print("dependent trx.",tx)
    print("total contract trx.", contract)
    graph.print_graph()