import random

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        # Add an item to the end of the queue (back of the line)
        self.items.append(item)

    def dequeue(self):
        # Remove and return the item from the front of the queue (FIFO)
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue.")
        return self.items.pop(0)

    def peek(self):
        # Return the front item without removing it
        if self.is_empty():
            raise IndexError("Cannot peek into an empty queue.")
        return self.items[0]

    def is_empty(self):
        # Return True if there are no items in the queue
        return len(self.items) == 0

    def select_and_announce_winner(self):
        """
        Randomly selects a winner from the queue.
        Dequeues all items up to and including the winner.
        Returns the name of the winning customer.
        """
        if self.is_empty():
            raise ValueError("Cannot select a winner from an empty queue.")

        # Pick a random index from the current queue
        winner_index = random.randint(0, len(self.items) - 1)
        winner_name = self.items[winner_index]

        # Dequeue everyone up to and including the winner
        for _ in range(winner_index + 1):
            self.dequeue()

        print(f"🎉 The winner is: {winner_name}!")
        print(f"   Customers remaining in queue: {len(self.items)}")
        return winner_name