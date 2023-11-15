class Counter:
    def __init__(self, counter, limit):
        self.counter = counter
        self.limit = limit
    def increment(self):
        if self.counter < limit:
            self.counter += 1
    def decrement(self)
        if self.counter > 0:
            self.counter -= 1
    def get_value(self):
        return self.counter

