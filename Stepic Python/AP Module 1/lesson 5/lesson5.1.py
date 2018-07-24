class MoneyBox:
    def __init__(self, capacity = 20):
        self.value = 0
        self.capacity = capacity
    def add(self, x):
        if self.can_add(x):
            self.value += x
    def can_add(self, v):
        return self.value + v <= self.capacity
mb = MoneyBox()
