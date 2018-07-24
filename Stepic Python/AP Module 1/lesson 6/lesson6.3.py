class ExtendedStack(list):
    def sum(self):
        self.append(self.pop() + self.pop())

    def sub(self):
        self.append(self.pop() - self.pop())

    def mul(self):
        self.append(self.pop() * self.pop())

    def div(self):
        self.append(self.pop() // self.pop())
inst = ExtendedStack([1, 2, 3, 4, 5, 6])
inst.sum()
print(inst)
inst.sub()
print(inst)
inst.mul()
print(inst)
inst.div()
print(inst)
