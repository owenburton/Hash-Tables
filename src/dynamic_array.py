class DynamicArray:
    def __init__(self, capacity=1):
        self.count = 0 # Number of elements in the array 
        self.capacity = capacity # Total amount of storage in the array
        self.storage = [None] * capacity

    def insert(self, index, value):
        