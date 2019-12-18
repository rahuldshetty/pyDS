class Queue:

    def __init__(self):
        self.__queue = []
        self.__front = 0
        self.__rear = -1

    def rear(self):
        if self.__rear >= self.__front:
            return self.__queue[self.__rear]
        else:
            raise Exception("Queue Empty")

    def front(self):
        try:
            return self.__queue[self.__front]
        except:
            raise Exception("Queue Empty")

    def enqueue(self,item):
        self.__rear += 1
        self.__queue.append(item)
    


    def dequeue(self):
        if self.length() == 0:
            raise Exception("Queue Empty")
        else:
            ele = self.__queue[self.__front]
            self.__front += 1
            return ele

    def print_(self):
        print(self.__queue)

    def length(self):
        return self.__rear - self.__front + 1

    

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    print(queue.front(),queue.rear(),queue.length())
    print(queue.dequeue())
    print(queue.length())
    print(queue.dequeue())
    print(queue.length())
    print(queue.dequeue())