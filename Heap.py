class MaximumHeap:
    Heap = []
    size = 0
    maxsize = 0

    def __init__(self, maxsize):

        self.maxsize = maxsize
        self.size = 0

        # Create an empty max heap with the given maximum capacity.
        self.Heap = [0 for i in range(self.maxsize + 2)]

        self.Heap[0] = 99999999

    def find_parent(self, position):

        # The position of parent node will return by this function

        return int(position / 2)

    def find_leftChild(self, position):

        # The position of left child will returned by this function

        return 2 * position

    def find_rightChild(self, position):

        # # The position of left child will returned by this function

        return 2 * position + 1

    def isLeaf(self, position):

        # If the value at the specified location is a leaf, this method will return true.

        if position > (self.size / 2) and position <= self.size:
            return True
        return False

    def swap(self, fposition, sposition):

        # This function swaps the heap's fposition and sposition values.

        self.Heap[fposition], self.Heap[sposition] = self.Heap[sposition], self.Heap[fposition]

    def MaximumHeapify(self, position):

        # The provided node location is checked to see if it is a leaf node.
        if self.isLeaf(position):
            return None

        left = self.find_leftChild(position)  # Getting left child of the supplied node
        right = self.find_rightChild(position)  # Getting right child of the supplied node

        #To see if the left or right nodes are greater than the parent node.
        if self.Heap[position] < self.Heap[left] or self.Heap[position] < self.Heap[right]:

            if self.Heap[left] > self.Heap[right]:
                self.swap(position, left)
                # If the left node is greater than the parent and right node, the left node is swapped with the parent node.

                self.MaximumHeapify(left)  # Making a recursive call with left node position

            else:
                self.swap(position, right)
                #If the right node is greater than the parent and the left node, the right node is swapped with the parent node.

                self.MaximumHeapify(right)  # Making a recursive call with right node position

    def insert(self, element):
        self.size += 1
        self.Heap[self.size] = element;  # Inserting the element at the leaf.

        current = self.size

        # Iterating across the heap until the inserted node's value is larger than the current parent node's value.
        while self.Heap[current] > self.Heap[self.find_parent(current)]:
            self.swap(current, self.find_parent(current))  # Swapping value of inserted node with current parent node.

            current = self.find_parent(current)  # Getting the value of parent node of current node.

    def print_heap(self):

        #printing the heap

        i = 1
        while i <= self.size / 2:
            print(f"PARENT : {self.Heap[i]}", end="|")
            print(f"LEFT CHILD : {self.Heap[2 * i]}", end="|")
            print(f"RIGHT CHILD : {self.Heap[2 * i + 1]}")
            i += 1

    def ExtractMaximum(self):
        max_val = self.Heap[1]  # Getting the Value of Root node (It will be maximum vlaue since it is max heap).
        self.size -= 1
        self.Heap[1] = self.Heap[self.size]  # Swapping the value of Root with leaf node.
        self.Heap.pop(self.size)  # Deleting the value of heap node from array.

        # Checking if the node is the root node.
        if self.size > 1:
            self.MaximumHeapify(1)  # maxHeapifing the heap so that all the nodes are in correct position.
        return max_val  # Returning the previously extracted max value.



# Driver Code
if __name__ == "__main__":
    print("The Max Heap is ")
    size = 9
    MaximumHeap = MaximumHeap(size)
    MaximumHeap.insert(1)
    MaximumHeap.insert(5)
    MaximumHeap.insert(90)
    MaximumHeap.insert(11)
    MaximumHeap.insert(86)
    MaximumHeap.insert(27)
    MaximumHeap.insert(8)
    MaximumHeap.insert(20)
    MaximumHeap.insert(7)

    MaximumHeap.print_heap()
    print()

    print(f"Extracted Max Value: {MaximumHeap.ExtractMaximum()}")
    MaximumHeap.print_heap()
    print()

    print(f"Extracted Max Value: {MaximumHeap.ExtractMaximum()}")
    MaximumHeap.print_heap()


