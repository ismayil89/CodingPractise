__author__ = "Mohamed Ismayil"
__credits__ = ["William Fiset"]
__version__ = "1.0"
__maintainer__ = "Mohamed Ismayil"
__email__ = "ismayil.ece@gmail.com"
__status__ = "Prototype"
__date__ = "19-Dec-2020"

class Queue:
    """
    Queue implementation using Array/List
    """

    def __init__(self):
        self.size = 0
        self.capacity = 20
        self.queue = self.capacity * [None]

    def sizeOf(self):
        return self.size

    def isEmpty(self):
        """
        Returns True/False based on Array Content
        """
        return self.size == 0

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is Empty")

        data = self.queue[0]
        tmp_queue = self.capacity * [None]
        tmp_idx = 0
        for idx in range(1, self.size):
            tmp_queue[tmp_idx] = self.queue[idx]
            tmp_idx += 1
        self.queue = tmp_queue
        self.size -= 1
        return data

    def enqueue(self, data):
        if self.size == 20:
            raise Exception("Queue is Full")

        self.queue[self.size] = data
        self.size += 1
        return self.size

    def peek(self):
        if self.size == 0:
            raise Exception("Queue is Empty")

        return self.queue[0]

    def clear(self):
        if not self.isEmpty():
            self.queue = self.capacity * [None]
            self.size = 0

        return self.size == 0

    def iterator(self):
        if self.isEmpty():
            raise Exception("Queue is Empty")

        iter = 0
        while iter < self.size:
            yield self.queue[iter]
            iter += 1
