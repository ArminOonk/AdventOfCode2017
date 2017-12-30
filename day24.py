class Piece:
    def __init__(self, txt):
        self.in_port = -1
        self.out_port = -1
        self.source = txt.strip()
        self.ports = list(map(int, txt.strip().split('/')))
        self.ports.sort()
        self.strength = sum(self.ports)
        self.children = []
        self.parent = None

    def connect(self, other):
        if self.out_port in other.ports:
            # Check if we are not already used
            p = self
            while p:
                if other.source == p.source:
                    # print('Already in the list')
                    return None
                p = p.parent

            # print('connection ' + str(self.out_port) + ' to ' + str(other.ports) + ' ' + other.source)

            other_copy = Piece(other.source)
            other_copy.in_port = self.out_port
            index = other_copy.ports.index(self.out_port)
            other_copy.out_port = other_copy.ports[(index + 1) % 2]

            self.children.append(other_copy)
            other_copy.parent = self
            return other_copy
        return None

    def chain_to_start(self):
        ret = []
        p = self
        while p:
            ret.append(p)
            p = p.parent
        return ret

    def chain_str(self):
        chain = self.chain_to_start()
        txt = []

        for c in chain[::-1]:
            txt.append(str(c.in_port) + '/' + str(c.out_port))

        return 'Strength: ' + str(self.chain_strength()) + ' ' + ' '.join(txt)

    def chain_strength(self):
        chain = self.chain_to_start()
        return sum([x.strength for x in chain])

    def chain_length(self):
        return len(self.chain_to_start())


with open('day24Input.txt', 'r') as f:
    data = f.readlines()

piece_start = Piece('0/0')
piece_start.in_port = 0
piece_start.out_port = 0

piece_list = []


for d in data:
    piece_list.append(Piece(d))

next_list = [piece_start]
end_list = []
while next_list:
    new_next_list = []
    for nl in next_list:

        for pl in piece_list:
            new_piece = nl.connect(pl)
            if new_piece:
                new_next_list.append(new_piece)
        if not nl.children:
            end_list.append(nl)
    next_list = new_next_list

# for el in end_list:
#     print(el.chain_str())

print('Strongest bridge: ' + str(max([x.chain_strength() for x in end_list])))
longest_bridge = max([x.chain_length() for x in end_list])
longest_bridge_list = [x for x in end_list if x.chain_length() == longest_bridge]

print('Longest bridge: ' + str(longest_bridge) + ' max strength: ' + str(max([x.chain_strength() for x in longest_bridge_list])))
