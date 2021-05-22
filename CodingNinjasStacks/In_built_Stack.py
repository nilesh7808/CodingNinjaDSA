import queue
# # # # in-built Stack
s = [1,2,3]
s.append(4)
s.append(5)
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s)

#
# # #inbuilt Queue
q = queue.Queue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)
while not q.empty():
    print(q.get())

# # Queue as an stack
q = queue.LifoQueue()
q.put(1)
q.put(2)
q.put(3)
while not q.empty():
    print(q.get())

x = [1,2,3,4,5]+
y = [6, 7,8,9]
print(x.append(y))