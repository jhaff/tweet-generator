#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        O(n^2) always iterates through the hash table in a nested for loop"""
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        O(n). Iterates through the hash table in a for loop"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        O(n) because you must traverse all buckets and all keys within buckets
        to get the length of each.
        If you use the .size property, then it would be O(b)"""
        counter = 0
        for bucket in self.buckets:
            for key, value in bucket.items():
                counter += 1 #increment our counter
        return counter

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        O(1) constant time complexity because you simply access a key
        *Though because we are using "in" items, so is that a loop?
        Yes, but we are only looping through the (few) items in that bucket"""
        #find the bucket (ll) that has our key in it
        bucket = self.buckets[self._bucket_index(key)]
        # if key is in the bucket corresponding to its bucket index
        # def matches_key(entry):
        #     return entry[0] == key
        #variable storing a function to be called later
        # matches_key = lambda entry: entry[0] == key
        # #find the entry containing the key we're looking for
        # entry = bucket.find(quality=matches_key)
        entry = bucket.find(quality=lambda entry: entry[0] == key)

        return entry is not None

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        O(1)"""
        if self.contains(key):
            #find the bucket (ll) that has our key in it
            bucket = self.buckets[self._bucket_index(key)]
            #search for the value associated with that key within that bucket

            entry = bucket.find(quality=lambda entry: entry[0] == key)
            #...
            return entry[1] #return just the value of our entry
        raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        O(1)"""
        # find the bucket (ll) that has our key in it
        bucket = self.buckets[self._bucket_index(key)]
        if self.contains(key):  # update existing entry
            #find the entry containing the key we're looking for
            entry = bucket.find(quality=lambda entry: entry[0] == key)
            # replace the found key with the new value
            bucket.replace(target=entry, replacement=(key, value))
        else:  # insert a new entry
            bucket.append(item=(key, value))


    def delete(self, given_key):
        """Delete the given key from this hash table, or raise KeyError.
        O(n^2). It iterates through the hash table in a nested for loop (innefficient)"""
        for bucket in self.buckets:
            for key, value in bucket.items():
                if key == given_key:
                    bucket(key[1]) == None #wipe out the value
                    bucket(key[0]) == None #wipe out the key itself.

        #TODO: however, does this just leave a hole?? what

        # raise KeyError('Key not found: {}'.format(key)) unsure where to put


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 11)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))
    ht.set('X',10)
    print('hash table: {}'.format(ht))
    return "yay"

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
