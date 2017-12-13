class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        self.min = None

    def set_min(self, min_val):
        self.min = min_val

    def get_min(self):
        return 'Empty' if not self.min else self.min
