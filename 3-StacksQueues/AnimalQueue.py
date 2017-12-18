from Queue import Queue


class AnimalQueue:

    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()
        self.timestamp = 0

    def enqueue(self, name, type):
        self.timestamp += 1

        if type == 'dog':
            self.dogs.enqueue(name, self.timestamp)
        elif type == 'cat':
            self.cats.enqueue(name, self.timestamp)


    def dequeueAny(self):
        return self.peek()


    def dequeueDog(self):
        if self.dogs.isEmpty():
            return 'No dogs left'

        return self.dogs.dequeue()

    def dequeueCat(self):
        if self.cats.isEmpty():
            return 'No cats left'

        return self.cats.dequeue()

    def peek(self):
        cat = self.cats.peek()
        dog = self.dogs.peek()

        if dog and cat:
            return self.dequeueDog() if dog.timestamp < cat.timestamp else self.dequeueCat()
        elif not cat:
            return self.dequeueDog()
        elif not dog:
            return self.dequeueCat()
        else:
            return 'No animals left'

    def isEmpty(self):
        return self.dogs.isEmpty() and self.cats.isEmpty()
