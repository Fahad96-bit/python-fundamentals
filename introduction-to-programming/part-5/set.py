# s2 = set({1, 2})
# print(s2)


# ✅ What is a Set in Python?

# A set is like a dictionary without values — it’s just a collection of unique items.

# Key points:

# No duplicates → each item appears only once.

# Unordered → no index, can’t access by position.

# Mutable → you can add or remove items.

# Supports math operations → union, intersection, difference


# s.add(5)
# print(s)  # {1, 2, 3, 4, 5}

# s.remove(2)   # removes 2, error if not found
# s.discard(10) # removes 10 if exists, no error


# a = {1, 2, 3}
# b = {3, 4, 5}

# print(a | b)  # Union → {1,2,3,4,5}
# print(a & b)  # Intersection → {3}
# print(a - b)  # Difference → {1,2}
# print(a ^ b)  # Symmetric Difference → {1,2,4,5}


# 1️⃣ List membership check (in)
# lst = [1,2,3,4,5]
# print(5 in lst)


# Python checks each element one by one until it finds a match.

# Worst case: it checks all elements → O(n) time

# For millions of items, this can be slow.


# 2️⃣ Set membership check (in)
# s = {1,2,3,4,5}
# print(5 in s)


# Sets in Python are implemented using hash tables.

# Each element has a hash value that tells Python exactly where to look.

# So checking if an element exists is O(1) time (constant time)

# Think of it like a phonebook with exact address — you go straight to the name, no searching.

# 3️⃣ Why sets are so fast

# Each element → hash → goes to a bucket

# To check membership → calculate hash → directly go to the bucket → check element

# No need to check every element

# Example:

# Set: {1,2,3,4,5}
# Hash table: bucket[hash(5)] → directly contains 5 → yes!
