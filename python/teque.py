import sys
# q = []

# # class Node:
# #     def __init__(self, val):
# #         self.val = val
# #         self.next = None
# #         self.prev = None
# #         self.index = None
# # class Teque:
# #     def __init__(self):
# #         self.head = None
# #         self.tail = None
    
# #     def push_back(self, val):
# #         node = Node(val)
# #         if self.head is None:
# #             self.head = self.tail = node
# #             return
# #         node.prev = self.tail
# #         self.tail.next = node
# #         self.tail = node
    
# #     def push_front(self, val):
# #         node = Node(val)
# #         if self.head is None:
# #             self.head = self.tail = node
# #         node.next = self.head
# #         self.head.prev = node
# #         self.head = node
            
# #     def 
        

# q = []
# opss = [x for x in sys.stdin]
# for ops in opss:
#     if len(ops.strip()) == 1:
#         continue
    
#     op = ops.strip().split()
#     if op[0] == 'push_back':
#         q.append(int(op[1]))
#     elif op[0] == 'push_front':
#         q.insert(0, int(op[1]))
#     elif op[0] == 'push_middle':
#         if len(q) % 2 == 0:
#             q.insert(len(q) // 2, int(op[1]))
#         else:
#             q.insert((len(q) // 2) + 1, int(op[1]))

#     elif op[0] == 'get':
#         print(q[int(op[1])])

class Teque:
    def __init__(self):
        self.front = []
        self.middle = []
        self.back = []

    def push_front(self, item):
        self.front.append(item)
        self._rebalance()

    def push_back(self, item):
        self.back.append(item)
        self._rebalance()

    def push_middle(self, item):
        self.middle.append(item)
        self._rebalance()

    def pop_front(self):
        if self.front:
            return self.front.pop(0)
        elif self.middle:
            return self.middle.pop(0)
        elif self.back:
            return self.back.pop(0)
        else:
            raise IndexError("Teque is empty")

    def pop_back(self):
        if self.back:
            return self.back.pop()
        elif self.middle:
            return self.middle.pop()
        elif self.front:
            return self.front.pop()
        else:
            raise IndexError("Teque is empty")

    def _rebalance(self):
        while len(self.front) - len(self.back) > 1:
            self.back.insert(0, self.front.pop())
        while len(self.back) - len(self.front) > 1:
            self.front.append(self.back.pop(0))
        while len(self.middle) - len(self.front) > 1:
            self.front.append(self.middle.pop(0))
        while len(self.front) - len(self.middle) > 1:
            self.middle.insert(0, self.front.pop())
        while len(self.middle) - len(self.back) > 1:
            self.back.insert(0, self.middle.pop())
        while len(self.back) - len(self.middle) > 1:
            self.middle.append(self.back.pop(0))

    def get_item(self, index):
        if index < len(self.front):
            return self.front[index]
        index -= len(self.front)
        if index < len(self.middle):
            return self.middle[index]
        index -= len(self.middle)
        if index < len(self.back):
            return self.back[index]
        raise IndexError("Index out of range")
    

def main():
    opss = [x for x in sys.stdin]
    q = Teque()

    for ops in opss:
        if len(ops.strip()) == 1:
            continue
        
        op = ops.strip().split()
        if op[0] == 'push_back':
            q.push_back(int(op[1]))
        elif op[0] == 'push_front':
            q.push_front(int(op[1]))
        elif op[0] == 'push_middle':
            q.push_middle(int(op[1]))
        elif op[0] == 'get':
            print(q.get_item(int(op[1])))

main()