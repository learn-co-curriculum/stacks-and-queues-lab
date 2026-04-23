import random

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        # Add an item to the end of the queue (FIFO)
        self.items.append(item)

    def dequeue(self):
        # Remove and return the item from the front of the queue
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def peek(self):
        # Return the front item without removing it
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        # Return True if queue has no items
        return len(self.items) == 0

    def select_and_announce_winner(self):
        """
        Randomly selects a winner from the queue.
        Dequeues all items up to and including the winner.
        Returns the name of the winning customer.
        """

        if self.is_empty():
            return None

        # Pick a random winner from current queue
        winner = random.choice(self.items)

        print(f"🎉 Winner selected: {winner}")

        removed = []

        # Dequeue until we reach the winner
        while not self.is_empty():
            person = self.dequeue()
            removed.append(person)

            if person == winner:
                break

        print(f"🧾 Removed from queue: {removed}")

        return winner