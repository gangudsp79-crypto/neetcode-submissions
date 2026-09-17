class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        # Dummy nodes
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    # Remove a node from the linked list
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # Add node just before tail
    # This means the node becomes Most Recently Used
    def add(self, node):
        prev = self.tail.prev

        prev.next = node
        node.prev = prev

        node.next = self.tail
        self.tail.prev = node

    def get(self, key):

        # Key doesn't exist
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Move it to MRU position
        self.remove(node)
        self.add(node)

        return node.value

    def put(self, key, value):

        # Key already exists
        if key in self.cache:
            node = self.cache[key]

            # Remove old node
            self.remove(node)

            # Update value
            node.value = value

            # Make it most recently used
            self.add(node)

        else:
            # Create new node
            node = Node(key, value)

            # Store in HashMap
            self.cache[key] = node

            # Add to linked list
            self.add(node)

            # Cache is too large
            if len(self.cache) > self.capacity:

                # Least recently used node
                lru = self.head.next

                self.remove(lru)

                # Remove from HashMap
                del self.cache[lru.key]