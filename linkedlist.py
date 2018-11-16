class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)

class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0  # how many nodes in our linked list
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty.
        O(1) because it's a simple variable check"""
        return self.head is None #No head, empty linkedlist.

    def length(self):
        """Return the length of this linked list.
        O(1) because it's a simple variable check.
        If we traversed its nodes to get the length, this would be O(n)"""
        return self.size #using our instance variable set above

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(1) because we simply replace the tail, and not loop
        through the whole list."""
        # Create new node to hold given item
        new_node = Node(item)
        # Append node after tail, if it exists
        if self.tail is not None:
            self.tail.next = new_node #extend list one past the tail, inserting node
            self.tail = new_node #reset the tail to the new correct node
        else: #if the list is empty, the head and tail is the same node.
            self.head = new_node
            self.tail = new_node
        self.size += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(1) because we simply replace the head and link it
        rather than running through the whole linkedlist"""
        new_node = Node(item)
        # Prepend node before head, if it exists
        if self.head is not None:
            new_node.next = self.head #move over the self.head and put node in front
            self.head = new_node #reset the head to the new correct node
        else: #if the list is empty, the head and tail is the same node.
            self.head = new_node
            self.tail = new_node
        self.size += 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case: O(1) if head is a match and has quality
        Worst case: O(size) if tail is the only node with the given quality"""
        node = self.head
        while node is not None:
            if quality(node.data): #if the .data of the current node has quality
                return node.data #return it
            node = node.next #move on to the next node

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) when the item to delete is the head.
        Worst case running time: O(size) when the item to del is the tail"""
        # Loop through all nodes to find one whose data matches given item
        # Update previous node to skip around node with matching data
        # Otherwise raise error to tell user that delete has failed
        # raise ValueError('Item not found: {}'.format(item))

        #initialize variables
        previous = None #to keep track of the node behind the node we're checking
        found = False #condition for the while loop
        node = self.head #initialize node to the head
        while not found and node is not None:
            if node.data == item:
                # if NOT at the head, link the previous node with the next one
                if previous is not None:
                    previous.next = node.next #skips over node, leaving it linkless
                # if it IS at the head, point the head to the next node
                else:
                    self.head = node.next
                # if at the tail, point the tail to the previous node
                if node.next is None:
                    self.tail = previous
                self.size -= 1
                found = True
            previous = node #store the current node in the previous variable
            node = node.next #move on
        if not found:
            raise ValueError('Item not found: {}'.format(item))

    def replace(self, target, replacement):
        # iterate through linked list until we find the target, then replace the data
        found = False #condition for the while loop
        node = self.head #initialize node to the head
        while not found and node is not None:
            if node.data == target: #if current node's data matches our target
                node.data = replacement #swap out the data for the replacement
                found = True #stop the loop
            node = node.next #move on
        if not found:
            raise ValueError('Replacement target not found: {}'.format(target))

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
