class Node:
    def __init__(self, txt):
        vals = txt.split()

        self.node_name = vals[0]
        w_txt = vals[1]

        self.weight = int(w_txt[1:(len(w_txt)-1)])

        if len(vals) > 3:
            self.children = ''.join(vals[3:]).split(',')
        else:
            self.children = []

    def __str__(self):
        c_txt = ', '.join(self.children)
        if c_txt:
            c_txt = ' -> ' + c_txt
        return self.node_name + ' (' + str(self.weight) + ') ' + c_txt


with open('day07Input.txt', 'r') as f:
    data = f.readlines()

nodes = []
for d in data:
    nodes.append(Node(d))

# walk to parent
current_node = nodes[0]
prev_node = nodes[0]
while True:
    for n in nodes:
        if current_node.node_name in n.children:
            current_node = n
            break

    if current_node == prev_node:
        break
    prev_node = current_node
print('Parent: ' + str(current_node))