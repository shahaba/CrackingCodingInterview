# Animal Shelter: enqueue, dequeueAny, dequeueDog, dequeueCat, isEmpty
from AnimalQueue import AnimalQueue

D = 'dog'
C = 'cat'

if __name__ == '__main__':

    animal_queue = AnimalQueue()

    print(animal_queue.dequeueAny())
    animal_queue.enqueue('charles', D)
    animal_queue.enqueue('kit', D)

    print(animal_queue.dequeueDog())
    print(animal_queue.dequeueCat())
