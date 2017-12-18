class Generator:
    def __init__(self, factor, first, sanity_check):
        self.factor = factor
        self.current = first
        self.sanity_check = sanity_check

    def run(self):
        self.current = (self.current * self.factor % 2147483647)
        while (self.current % self.sanity_check) != 0:
            self.current = (self.current * self.factor % 2147483647)
        return self.current

    def compare_16bit(self, other):
        return self.current & 0xffff == other.current & 0xffff


gen_a_factor = 16807
gen_b_factor = 48271
# Example
# a = Generator(factor=16807, first=65, sanity_check=4)
# b = Generator(factor=48271, first=8921, sanity_check=8)
# Input
a = Generator(factor=16807, first=277, sanity_check=4)
b = Generator(factor=48271, first=349, sanity_check=8)

print('a\t\tb')
score = 0
for _ in range(0, 5000000):
    a.run()
    b.run()
    # print(str(a.current) + '\t\t' + str(b.current))
    if a.compare_16bit(b):
        # print("Match! 16bit")
        score += 1
    if (_ % 200000) == 0:
        print(str(_))
print('Score: ' + str(score))
