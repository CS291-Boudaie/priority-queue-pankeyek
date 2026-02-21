# In this file, you will develop a Min Heap to use in a priority queue.
# A priority queue is a fundamental data structure for many of the algorithms we will cover in this class,
# so it is important to get the fundamentals right.

# In a normal queue, you insert items, and they are removed in first-in, first-out order (FIFO).
# In a priority queue, you insert an arbitrary object AND a priority value for that item.
# When an item is requested, the item with the lowest priority value is returned (and removed).
# Read more: https://en.wikipedia.org/wiki/Priority_queue

# Fundamental to the Priority Queue is the "Heap" data structure.
# Heaps (especially min-heaps) allow for fast retrieval of the smallest-priority element,
# and efficient re-ordering after inserts/removals.
# Once you have a heap, implementing a Priority Queue is straightforward.

# A min-heap can be thought of as a binary tree where each node has priority <= its children.
# This means the smallest-priority element will always be at index 0.

# The tree is stored in a list. For a node at index i:
# left child index = 2*i + 1
# right child index = 2*i + 2
# parent index = (i - 1) // 2

# When you add an item, append it to the end of the list, then "bubble up"
# by swapping it with its parent while it has a smaller priority than the parent.

# When you pop the minimum item, you remove and return the item at index 0.
# Then move the last element to index 0 and "bubble down" by swapping with the smaller child
# until the heap property is restored.

# Read more: https://en.wikipedia.org/wiki/Heap_(data_structure)

# You can also watch this video, but note it starts indexing at 1 (different math).
# You may implement a 1-indexed heap if you want (leave index 0 unused), or use 0-indexing.
# Either approach works:
# https://www.youtube.com/watch?v=0wPlzMU-k00

# For this assignment, the items added to the priority queue can be any object.
# You will only compute/compare priorities (ints).
# For peek() and pop(), return (item, priority) as a tuple.

class MinHeap:
    def __init__(self):
        # We'll store elements as tuples: (priority, item)
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def peek(self):
        # TODO: Return (priority, item) but do NOT remove
        # If empty, return None (or raise an error)
        if self.is_empty():
            return None
        else:
            return self.data[0]

    def add(self, priority, item):
        # TODO: Add (priority, item) to end of list
        # Then bubble it UP into correct position
        self.data.append((priority, item))
        i = self.__len__() - 1
        while i > 0:
            if self.data[i][0] < self.data[(i-1)//2][0]:
                temp = self.data[i]
                self.data[i] = self.data[(i-1)//2]
                self.data[(i-1)//2] = temp
                i = (i-1)//2
            else:
                break
        

    def pop_min(self):
        # TODO: Remove and return the smallest element (priority, item)
        # Steps:
        # 1) swap root with last element
        # 2) pop last element (former root)
        # 3) bubble DOWN new root
        if self.is_empty():
            return None
        
        root = self.data[0]
        self.data[0] = self.data[self.__len__()-1]
        self.data[self.__len__()-1] = root

        root = self.data.pop()

        i = 0
        while i < self.__len__():
            if (i*2+1) < self.__len__() and self.data[i][0] > self.data[i*2+1][0]:
                if (i*2+2) < self.__len__() and self.data[i*2+1][0] <= self.data[i*2+2][0]:
                    temp = self.data[i]
                    self.data[i] = self.data[i*2+1]
                    self.data[i*2+1] = temp
                    i = i*2 + 1
                else:
                    if (i*2+2) < self.__len__():
                        temp = self.data[i]
                        self.data[i] = self.data[i*2+2]
                        self.data[i*2+2] = temp
                        i = i*2 + 2
                    else:
                        temp = self.data[i]
                        self.data[i] = self.data[i*2+1]
                        self.data[i*2+1] = temp
                        i = i*2 + 1
            elif (i*2+2) < self.__len__() and self.data[i][0] > self.data[i*2+2][0]:
                temp = self.data[i]
                self.data[i] = self.data[i*2+2]
                self.data[i*2+2] = temp
                i = i*2 + 2
            else:
                break
        return root
        

    def _bubble_up(self, idx):
        # TODO: Implement
        # Keep swapping this node with its parent while it has a smaller priority.
        # parent index = (idx - 1) // 2
        # Stop when you reach the root OR parent already has <= priority.
        i = idx
        while i > 0 and self.data[i][0] < self.data[(i-1)//2][0]:
            temp = self.data[i]
            self.data[i] = self.data[(i-1)//2]
            self.data[(i-1)//2] = temp
            i = (i-1)//2

    def _bubble_down(self, idx):
        # Keep swapping this node downward until the heap property is restored.
        # left child = 2*idx + 1, right child = 2*idx + 2
        # Find the smaller child, then swap if current priority is bigger.
        # Stop when no children exist OR current is <= both children.
        i = idx
        while i < self.__len__():
            if (i*2+1) >= self.__len__():
                break
            baby = i*2+1
            if (i*2+2) < self.__len__():
                if self.data[i*2+2][0] < self.data[i*2+1][0]:
                    baby = i*2+2
            if self.data[i][0] > self.data[baby][0]:
                temp = self.data[i]
                self.data[i] = self.data[baby]
                self.data[baby] = temp
                i = baby
            else:
                break
            
            


# Once you have a min heap, the priority queue is pretty straightforward. 
# Make sure you understand what it is doing

class PriorityQueue:
    def __init__(self):
        self.heap = MinHeap()

    def is_empty(self):
        return self.heap.is_empty()

    def add(self, priority, item):
        self.heap.add(priority, item)

    def pop(self):
        return self.heap.pop_min()

    def peek(self):
        return self.heap.peek()

    def __len__(self):
        return len(self.heap)
