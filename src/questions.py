# What is an array and how does it work?
# -Stores a sequence of elements
# -Each element must be the same data type
# -Occupies a contiguous block of memory
# -Can access data in constant time with this equation:
# memory_address = starting_address + index * data_size

# What is a hash function and how does it work?
# -Deterministic: For a given input, the output will always be the same.
# -Defined output range: For a hash table of size 16, 
# all keys must hash to a value 0-15. 
# For smaller values, this is usually accomplished using 
# the modulo % operation.
# -Predictable Speed: Hash functions for hash tables should 
# be lightning fast while cryptographic hashes 
# (like bcrypt) should be very slow.
# -Non-invertible: You should not be able to reconstruct 
# the input value from the output. This trait is important 
# cryptographic hashes but not necessary 
# for general hash tables.

# What is a hash table and how does it work?
# -Hash Tables have an underlying Array structure
# - This is why they are as fast at accessing elemetns as arrays
# -The main difference is that Hash Tables are indexed using a 
# hash function in an unordered fashion, 
# whereas arrays are indexed via contiguous ordered indices
# -HashTable code is fairly similar to DynamicArray code