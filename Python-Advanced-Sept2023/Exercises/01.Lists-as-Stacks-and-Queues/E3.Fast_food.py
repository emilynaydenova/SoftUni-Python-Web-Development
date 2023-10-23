from collections import deque

food_quantity = int(input())

orders_queue = deque([int(x) for x in input().split()])
print(max(orders_queue))

while food_quantity > 0 and orders_queue:
    if orders_queue[0] > food_quantity:
        print(f'Orders left: {" ".join([str(x) for x in orders_queue])}')
        break
    food_quantity -= orders_queue.popleft()
else:
    print('Orders complete')

#  -----------------------------------------------------------
# Ver 2
food_quantity = int(input())
# !!!!! input sequence of integers in deque
orders = deque([int(x) for x in input().split()])

print(max(orders))

while orders:
    order = orders.popleft()
    if food_quantity >= order:
        food_quantity -= order
    else:
        orders.appendleft(order)
        print(f"Orders left: {' '.join(str(x) for x in orders)}")
        break
else:
    print('Orders complete')

# ------------------------------------
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

    def max(self):
        return max(self.items)


food_quantity = int(input())
orders = list(map(int, input().split()))
q = Queue()
[q.enqueue(x) for x in orders]

print(q.max())

while not q.is_empty():
    if food_quantity >= q.peek():
        food_quantity -= q.dequeue()
    else:
        dd = 'Orders left:'
        while not q.is_empty():
            dd += ' ' + str(q.dequeue())
        print(dd)
        break
else:
    print('Orders complete')
