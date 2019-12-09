"""
We are given a stack data structure with push and pop operations, 
the task is to implement a queue using instances of stack data structure and operations on them.
"""

#SUDO CODE
# While stackA is not empty, push everything from stackA to stackB
# Push x to stackA (assuming size of stack is unlimited)
# Push everything back to stackA
# Time complexity will be O(n)

# If stackA is empty then error
# Pop an item from stackA and return it
# Time Complexity O(1)


class Queue:
    def __init__(self):
        self.stackA = []
        self.stackB = []

    # Time complexity will be O(n)
    def Push(self, value):
        # Moving the elements from StackA to StackB
        while len(self.stackA) != 0:
            self.stackB.append(self.stackA[-1])
            self.stackA.pop()

        # Push items into stackA
        self.stackA.append(value)

        # Push everything back to StackA
        while len(self.stackB) != 0:
            self.stackA.append(self.stackA[-1])
            self.stackB.pop

    # Time Complexity O(1)
    def Pop(self):
        # Check if is empty
        if len(self.stackA) == 0:
            print('Queue is Empty!')

        #Return top of StackA
        x = self.stackA[-1]
        self.stackA.pop()
        return x


if __name__ == '__main__':
    q = Queue()
    q.Push(1)
    q.Push(2)
    q.Push(3)
    q.Push(4)
    q.Push(5)

    print(q.Pop())
    print(q.Pop())
    print(q.Pop())
    print(q.Pop())
    print(q.Pop())