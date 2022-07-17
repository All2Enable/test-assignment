# Первый способ реализации FIFO через обычные списки. Он не эффективен из-за
# необходимости при удалении и добавлении сдвига элементов по списку, что отнимает
# много времени.
# Второй способ использует deque в качестве основы. Стандартная реализация очереди.
# Третий способ использует класс multiprocessing.Queue, что позволяет
# находящимся в очереди объектам быть обработанными параллельно несколькими
# одновременно работающими процессами.


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        return self.queue.insert(0, x)

    def dequeue(self):
        return self.queue.pop()

    def isEmpty(self):
        return len(self.queue) == 0

    def front(self):
        return self.queue[-1]

    def rear(self):
        return self.queue[0]


from collections import deque


class Queuedeq:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, x):
        return self.queue.appendleft(x)

    def dequeue(self):
        return self.queue.pop()

    def isEmpty(self):
        return len(self.queue) == 0

    def front(self):
        return self.queue[-1]

    def rear(self):
        return self.queue[0]


from multiprocessing import Queue


class multiQueue:
    def __init__(self):
        self.queue = Queue()

    def enqueue(self, x):
        return self.queue.put(x)

    def dequeue(self):
        return self.queue.get()

    def isEmpty(self):
        return self.queue.empty()
