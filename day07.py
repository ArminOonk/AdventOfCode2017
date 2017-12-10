class Node:
    def __init__(self, txt):
        vals = txt.split()

        self.node_name = vals[0]
        w_txt = vals[1]

        self.weight = int(w_txt[1:(len(w_txt)-1)])

        self.children = []

        if len(vals) > 3:
            self.children_str = ''.join(vals[3:]).split(',')
        else:
            self.children_str = []

    def stack_weight(self):
        weight = self.weight
        for c in self.children:
            weight += c.stack_weight()
        return weight

    def find_name(self, node_name):
        if self.node_name == node_name:
            return self

        for cn in self.children:
            ret = cn.find_name(node_name)
            if ret:
                return ret
        return None

    def __str__(self):
        child_name_list = []
        for cn in self.children:
            child_name_list.append(cn.node_name)

        c_txt = ', '.join(child_name_list)
        if c_txt:
            c_txt = ' -> ' + c_txt
        return self.node_name + ' (' + str(self.weight) + ') ' + c_txt


with open('day07Input.txt', 'r') as f:
    data = f.readlines()

nodes = []
for d in data:
    nodes.append(Node(d))

# build tree
for n in nodes:
    if n.children_str:
        for cn in n.children_str:
            for nn in nodes:
                if cn == nn.node_name:
                    n.children.append(nn)

# for n in nodes:
#     print(n)
# walk to parent
parent_node = nodes[0]
prev_node = nodes[0]
while True:
    for n in nodes:
        if parent_node.node_name in n.children_str:
            parent_node = n
            break

    if parent_node == prev_node:
        break
    prev_node = parent_node

# print('Parent: ' + str(parent_node) + ' stack weight: ' + str(parent_node.stack_weight()))
# print('-'*30)
#
# for c in parent_node.children:
#     print(str(c) + ' stack weight: ' + str(c.stack_weight()))
#
# print('-'*30)
wrong_weight = parent_node.find_name('pkowhq')
for c in wrong_weight.children:
    print(str(c) + ' stack weight: ' + str(c.stack_weight()))

# print_list = [parent_node]
# while print_list:
#     new_print_list = []
#     for pl in print_list:
#         sweights = []
#         txt = []
#         for c in pl.children:
#             sw = c.stack_weight()
#             sweights.append(sw)
#             txt.append(str(c) + ' stack weight: ' + str(sw))
#         if max(sweights) != min(sweights):
#             for t in txt:
#                 print(t)
#
#             new_print_list.append(c)
#     print('-' * 30)
#     print_list = new_print_list


