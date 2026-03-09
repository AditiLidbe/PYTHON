class BufferFullException(BufferError):
    def __init__(self, message):
        super().__init__(message)


class BufferEmptyException(BufferError):
    def __init__(self, message):
        super().__init__(message)


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def read(self):
        if self.size == 0:
            raise BufferEmptyException("Circular buffer is empty")

        data = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return data

    def write(self, data):
        if self.size == self.capacity:
            raise BufferFullException("Circular buffer is full")

        self.buffer[self.tail] = data
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def overwrite(self, data):
        if self.size == self.capacity:
            self.buffer[self.tail] = data
            self.tail = (self.tail + 1) % self.capacity
            self.head = (self.head + 1) % self.capacity
        else:
            self.write(data)

    def clear(self):
        self.buffer = [None] * self.capacity
        self.head = 0
        self.tail = 0
        self.size = 0