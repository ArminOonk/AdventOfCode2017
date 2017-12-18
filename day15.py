class Generator:
    def __init__(self, factor, first):
        self.factor = factor
        self.current = first

    def run(self):
        self.current = (self.current * self.factor % 2147483647)
        return self.current

    def compare_16bit(self, other):
        return self.current & 0xffff == other.current & 0xffff


gen_a_factor = 16807
gen_b_factor = 48271
# Example
# a = Generator(factor=16807, first=65)
# b = Generator(factor=48271, first=8921)
# Input
a = Generator(factor=16807, first=277)
b = Generator(factor=48271, first=349)

# print('a\t\tb')
score = 0
for _ in range(0, 40000000):
    a.run()
    b.run()
    # print(str(a.run()) + '\t\t' + str(b.run()))
    if a.compare_16bit(b):
        # print("Match! 16bit")
        score += 1
    if (_ % 1000000) == 0:
        print(str(_))
print('Score: ' + str(score))
