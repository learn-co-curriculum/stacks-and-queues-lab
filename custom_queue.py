import random

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.items:
            return self.items.pop(0)
        return None

    def peek(self):
        if self.items:
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def select_and_announce_winner(self):
        if not self.items:
            return None
        winner = random.choice(self.items)
        while self.items:
            removed = self.dequeue()
            if removed == winner:
                break
        return winner