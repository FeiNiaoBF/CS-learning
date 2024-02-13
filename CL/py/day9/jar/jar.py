class Jar:
    def __init__(self, capacity=12):
        self._size = 0;
        self._capacity = capacity

    def __str__(self):
        return '🍪' * self._size

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError("Jar is full")
        self._size += n

    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError("Jar is empty")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
