# import random

# class Queue:
#     def __init__(self):
#         self.items = []

#     def enqueue(self, item):
#         # TODO: Add an item to the end of the queue
#         pass

#     def dequeue(self):
#         # TODO: Remove and return the item from the front of the queue
#         pass

#     def peek(self):
#         # TODO: Return the item at the front of the queue without removing it
#         pass

#     def is_empty(self):
#         # TODO: Return True if the queue is empty
#         pass

#     def select_and_announce_winner(self):
#         """
#         Randomly selects a winner from the queue.
#         Dequeues all items up to and including the winner.
#         Returns the name of the winning customer.
#         """
#         # TODO: Implement winner selection and dequeue process
#         pass

import random

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        """Return the item at the front without removing it."""
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        """Return True if the queue is empty."""
        return len(self.items) == 0

    def select_and_announce_winner(self):
        """
        Randomly selects a winner from the queue.
        Dequeues all items up to and including the winner.
        Returns the name of the winning customer.
        """
        if self.is_empty():
            return None

        # Randomly choose a winner from current queue
        winner = random.choice(self.items)

        print(f"Winner selected: {winner}")

        # Remove customers until the winner is reached
        while not self.is_empty():
            customer = self.dequeue()

            print(f"Dequeued: {customer}")

            if customer == winner:
                break

        return winner
