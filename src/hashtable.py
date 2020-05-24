# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.num_stored_keys = 0


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        # Start from arbitrary large prime
        hash_value = 5381
        # Bit-shift & sum value for each char
        for c in key:
            hash_value = ((hash_value << 5) + hash_value) + c
        return hash_value


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert_no_resize(self, key, value, storage=None):
        if not storage:
            storage = self.storage
        node = storage[self._hash_mod(key)]
        while node:
            if node.key == key:
                node.value = value
                return
            if not node.next:
                node.next = LinkedPair(key, value)
                return
            node = node.next
        storage[self._hash_mod(key)] = LinkedPair(key, value)
        self.num_stored_keys += 1

    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        self.insert_no_resize(key, value)
        self.resize()


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        # '''
        node = self.storage[self._hash_mod(key)]
        if not node:
            print("Key not found") 
            return
        prev = None
        while node:
            if node.key == key:
                # if head
                if not prev:
                    self.storage[self._hash_mod(key)] = None
                    self.num_stored_keys -= 1
                    return 
                # if tail
                elif not node.next:
                    prev.next = None
                    return
                else:
                    prev.next = node.next
                    return
            prev = node
            node = node.next
        self.resize()


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        node = self.storage[self._hash_mod(key)]
        while node:
            if node.key == key:
                break
            node = node.next
        return node if not node else node.value


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        def copy_to_new_storage():
            new_storage = [None] * self.capacity
            self.num_stored_keys = 0
            for node in self.storage:
                if not node:
                    continue
                else:
                    while node:
                        self.insert_no_resize(node.key, node.value, new_storage)
                        node = node.next
            self.storage = new_storage

        # check load factor
        if self.num_stored_keys / self.capacity < 0.2:
            # shrink
            self.capacity = int(self.capacity / 2)
            copy_to_new_storage()
            
        if self.num_stored_keys / self.capacity > 0.7:
            # expand
            self.capacity *= 2
            copy_to_new_storage()
            






if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
