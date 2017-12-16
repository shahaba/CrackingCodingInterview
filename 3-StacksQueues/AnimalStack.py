from Stack import Stack
from Node import Node


class AnimalStack:

    def __init__(self):
        self.dog = Stack()
        self.cat = Stack()

    def push(self, type, name, age):
        if type == 'cat':
            ncat = Node(name)
            ncat.age = age
            self.cat.push(ncat)
        elif type == 'dog':
            ndog = Node(name)
            ndog.age = age
            self.dog.push(ndog)
